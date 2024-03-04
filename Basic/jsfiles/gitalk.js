const gitalk = new gitalk({
    clientID: '039ac37a309fe2e4cf1c',
    clientSecret: '8dbf2f3c2a26a12e3cc59ec8222fd01bcb2dce5b',
    repo: 'comments-repo',      // The repository of store comments,
    owner: 'wing0night',
    admin: ['wing0night'],
    id: location.pathname,      // Ensure uniqueness and length less than 50
    distractionFreeMode: false  // Facebook-like distraction free mode
  })
  
  gitalk.render('gitalk-container')

