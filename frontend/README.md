# Frontend

### Roadmap:
```
├── README.md
├── babel.config.js
├── package-lock.json
├── package.json            # all needed dependencies are here
├── public
│   ├── favicon.ico
│   └── index.html
├── src
│   ├── App.vue             # root component that just concat two available components
│   ├── assets
│   │   └── logo.png
│   ├── components          # components that we will test
│   │   ├── Counter.vue
│   │   └── HelloWorld.vue
│   └── main.js
└── tests                   # tests module lies here
    └── unit
        └── example.spec.js
```

# HOWTO

0. Install npm, then ``
1. Run `npm install` while being in `frontend/` folder
2. Run `npm test`

# Useful links

#### general
* https://vue-test-utils.vuejs.org/guides/#getting-started
* https://jestjs.io/ - jest framework for testing that we use
#### user behavior events
* https://vue-test-utils.vuejs.org/guides/#testing-key-mouse-and-other-dom-events

#### pure js and html
* https://dev.to/snowleo208/things-i-learned-after-writing-tests-for-js-and-html-page-4lja

#### testing vuex
* https://vue-test-utils.vuejs.org/guides/#testing-vuex-in-components

#### CI/CD with gitlab
* https://about.gitlab.com/2017/09/12/vuejs-app-gitlab/
