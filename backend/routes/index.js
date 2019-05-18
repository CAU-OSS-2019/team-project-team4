var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
var elasticsearch = require('elasticsearch');
var request = require('request');
var path = require('path');

router.use(bodyParser.urlencoded({extended: false}));

/** ElasticSearch */
var client = new elasticsearch.Client({
  host: '<elasticsearch url>',  // this will be changed as real ES domain
  //log: 'trace'
});

/** Twitch Dev Data */
var redirectURL = '<redirect url>';
var clientID = '<client id>';
var clientSecret = '<client secret>';

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
  req.session.save(function() {
    res.redirect('/');
  });
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
  // get information from current id
  client.search({
    index: 'entity',
    body: {
      query: {
        match: {
          userID: req.session.loginAccount
        }
      }
    },
    refresh: 'wait_for'
  }, function(searcherr, searchres) {
    console.log('search complete');
    // send data to frontend
    var searchResult = searchres.hits.hits;
    var resultData = [];
    for(var i = 0; i < searchres.hits.total; i++)
    {
      resultData.push(i);
      resultData[i] = [];
      resultData[i].push('id'); resultData[i].push('donatorID'); resultData[i].push('content'); resultData[i].push('status');
      resultData[i]['id'] = searchResult[i]._source.id;
      resultData[i]['donatorID'] = searchResult[i]._source.donatorID;
      resultData[i]['content'] = searchResult[i]._source.content;
      resultData[i]['status'] = searchResult[i]._source.status;
    }
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
  // update mission data
  client.updateByQuery({
    index: 'entity',
    body: {
      query: {
        match: {
          id: req.body.id // id data from frontend
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
  // update mission data
  client.updateByQuery({
    index: 'entity',
    body: {
      query: {
        match: {
          id: req.body.id // id data from frontend
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
  // delete mission data
  client.deleteByQuery({
    index: 'entity',
    body: {
      query: {
        match: {
          id: req.body.id //id data from frontend
        }
      }
    },
    refresh: 'wait_for'
  }, function(err, deleteres) {
    console.log('delete '+req.body.id+' mission successfully');
  });
});

module.exports = router;