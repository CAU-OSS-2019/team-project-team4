var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
var elasticsearch = require('elasticsearch');
var request = require('request');
var path = require('path');
var fs = require('fs');

router.use(bodyParser.urlencoded({extended: false}));
var spawn = require("child_process").spawn;
var idcount = 0 // for assign id to mission data

/** ElasticSearch */
var client = new elasticsearch.Client({
  host: '<es url>',  // this will be changed as real ES domain
  //log: 'trace'
});

/** Twitch Dev Data */
var redirectURL = '<redirect URL>';
var clientID = '<client ID>';
var clientSecret = '<client Secret>';

// check if python file is running
var bIsModelRun = false;

// Home page
router.get('/', function(req, res, next) {
  if(req.session.bIsLogined) // login already
  {
    res.redirect('/dashboard');
  }
  else
  {
    console.log(req.query);
    res.sendFile(path.join(__dirname, '../public', 'index.html'));
  }
});

/* Login, Logout: these will be made with Twitch API */
router.get('/login', function(req, res) {
  // Access control
  if(req.session.bIsLogined)
  {
    res.redirect('/dashboard');
    return false;
  }

  res.redirect('https://api.twitch.tv/kraken/oauth2/authorize?response_type=code&client_id='+clientID+'&redirect_uri='+redirectURL+'&scope=user:read:email');
});

// get user information
router.get('/twitch', function(req, res) {
  var code = req.originalUrl.substr(13, 30);
  request.post({
    url: 'https://id.twitch.tv/oauth2/token?client_id='+clientID+'&client_secret='+clientSecret+'&code='+code+'&grant_type=authorization_code&redirect_uri='+redirectURL
  }, function(err, resp, body) {
    oauthCode = JSON.parse(body);
    var oauth = 'Bearer '+oauthCode['access_token'];
    request.get({
      url: 'https://api.twitch.tv/helix/users',
      headers: {
        'Authorization': oauth
      }
    }, function(err, resp2, body2) {
      var userdata = JSON.parse(body2);
      // Create session
      req.session.bIsLogined = true;
      req.session.loginAccount = userdata['data'][0]['login'];
      req.session.displayname = userdata['data'][0]['display_name'];
      req.session.profile_image_url = userdata['data'][0]['profile_image_url'];
      req.session.save();
      console.log(req.session);
      res.redirect('/dashboard');
    })
  })
});

router.post('/logout', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  // Destroy session
  delete req.session.bIsLogined;
  delete req.session.loginAccount;
  delete req.session.displayname;
  delete req.session.profile_image_url;
  req.session.save();
  res.send('');
});

/* mission page */
router.get('/dashboard', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  res.sendFile(path.join(__dirname, '../public', 'index.html'));
});

router.post('/get_result', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  // get misssions from model
  var currentPath = path.join(__dirname, '../missionResult.json');
  fs.readFile(currentPath, async function(err, data)
  {
    var result = JSON.parse(data.toString());
    console.log(result);
    var i = 0;
    if(bIsModelRun == false && result.length > 0) {runModel(result[i].content, i, result); bIsModelRun = true;}
  });

  // get information from current id
  client.search({
    index: 'entity',
    body: {
      query: {
        match: {
          streamerID: req.session.loginAccount
        }
      }
    }
  }, function(searcherr, searchres) {
    console.log('search complete');
    // send data to frontend
    var resultData = [];
    if(searchres.hits != null)
    {
      var searchResult = searchres.hits.hits;
      for(var i = 0; i < searchres.hits.total; i++)
      {
        resultData.push(i);
        resultData[i] = [];
        resultData[i].push(searchResult[i]._id);
        resultData[i].push(searchResult[i]._source.donatorID);
        resultData[i].push(searchResult[i]._source.content);
        resultData[i].push(searchResult[i]._source.status);
      }
    }
    //console.log(resultData);
    res.send(resultData);
  });
});

router.post('/mission_success', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  console.log('mission success: '+req.body.id);
  // update mission data
  client.updateByQuery({
    index: 'entity',
    body: {
      query: {
        match: {
          _id: req.body.id // id data from frontend
        }
      },
      script: {
        inline: 'ctx._source.status = '+"\'success\'"
      }
    },
    refresh: 'wait_for'
  }, function(err, updateres) {
    console.log('update mission to "success" successfully');
  });
});

router.post('/mission_fail', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  console.log('mission fail: '+req.body.id);
  // update mission data
  client.updateByQuery({
    index: 'entity',
    body: {
      query: {
        match: {
          _id: req.body.id // id data from frontend
        }
      },
      script: {
        inline: 'ctx._source.status = '+"\'fail\'"
      }
    },
    refresh: 'wait_for'
  }, function(err, updateres) {
    console.log('updata mission to "fail" successfully');
  });
});

router.post('/mission_delete', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  console.log('mission delete: '+req.body.id);
  // delete mission data
  client.deleteByQuery({
    index: 'entity',
    body: {
      query: {
        match: {
          _id: req.body.id //id data from frontend
        }
      }
    },
    refresh: 'wait_for'
  }, function(err, deleteres) {
    console.log('delete '+req.body.id+' mission successfully');
  });
});

router.post('/get_userinfo', function(req, res) {
  // Access control
  if(!req.session.bIsLogined)
  {
    res.redirect('/');
    return false;
  }
  var userinfo = [req.session.displayname, req.session.profile_image_url];
  console.log(userinfo);
  res.send(userinfo);
});

function runModel(missionstr, i, result) {
  var filePath = path.join(__dirname, '../load_model_and_predict.py');
  var process = spawn('python3', [filePath, missionstr]);  //python3
  console.log(missionstr);
  var bIsMission;
  process.stdout.on('data', function(data) {
    bIsMission = data.toString();
  });
  process.stdout.on('end', function() {
    if(bIsMission == 0)
    {
      idcount++;
      console.log('미션입니다' + i);
      console.log(idcount);
      client.bulk({
        body: [
          {"index": {"_index": "entity", "_type": "mission", "_id": "vo2qjsld-"+idcount}},
          {
            "streamerID": 'vo2qjsld',//result[i].streamerID,
            "donatorID": result[i].donatorID,
            "content": result[i].content,
            "status": "mission"
          }
        ]
      }, function(err, createres) {
        console.log(createres);
      })
    }
    else {console.log('미션이 아닙니다');}

    i++;
    if(i < result.length) {runModel(result[i].content, i, result);}
    else {bIsModelRun = false;}
  });
}

module.exports = router;