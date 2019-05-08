var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
var elasticsearch = require('elasticsearch');
var request = require('request');

router.use(bodyParser.urlencoded({extended: false}));

/** ElasticSearch */
var client = new elasticsearch.Client({
  host: '<ES URL>',  // this will be changed as real ES domain
  //log: 'trace'
});

/** Twitch Dev Data */
var redirectURL = '<Redirect URL>';
var clientID = '<Client ID>';
var clientSecret = '<Client Secret>';

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

/* Login, Logout: these will be made with Twitch API => no need to take get method */
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
  var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;
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
  res.send('Hello, ' + req.session.displayname);
  //res.sendFile(path.join(__dirname, '../public', 'index.html'));
});

router.post('/dashboard', function(req, res) {
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
          userID: req.session.id
        }
      }
    }
  }, function(searcherr, searchres) {
    console.log('search complete');
    // send data to frontend

    res.send('');
  });
});

module.exports = router;
