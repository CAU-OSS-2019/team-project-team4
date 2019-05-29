# Tission
![Tission](https://github.com/CAU-OSS-2019/team-project-team4/blob/front/front/vue-front/public/img/brand/tission2.png?raw=true)


We created the Tission site using the Aragon dashboard. The goal is to facilitate management by running the necessary lists on the web for Twitch mission management.

## Purpose of Tission
Tission is a broadcast support platform that helps Twitch TV broadcast on the web.
The platform we plan to provide is the ability to automatically analyze and list the sponsorship text of viewers. By automatically analyzing and classifying messages in real time, Streamer is focused on the practicality of both viewers and streamers, ensuring that mission data is seamlessly managed without disturbing the broadcast progress. We will provide the role of enhancing the quality of personal broadcasting contents by merging with existing broadcasting support platform through management function and analysis function.

## The fist page of Staring Tission
![Strating image of Tission](https://github.com/CAU-OSS-2019/team-project-team4/blob/front/front/vue-front/public/img/theme/first.PNG)

## List of using OpenSource
* [Vue-argon-dashboard](https://github.com/creativetimofficial/vue-argon-dashboard/)
* [vuejs/vue](https://github.com/vuejs/vue)
* [FontAwesome](https://github.com/FortAwesome/Font-Awesome)
* [BootStrap](https://github.com/twbs/bootstrap)


## Table of Contents

* [Versions](#versions)
* [Before you start](#Before-you-start)
* [Quick Start](#quick-start)
* [File Structure](#file-structure)
* [Browser Support](#browser-support)
* [Resources](#resources)
* [Licensing](#licensing)
* [Useful Links](#useful-links)

## Versions
<img src="https://github.com/creativetimofficial/public-assets/blob/master/logos/vue-logo.jpg?raw=true" width="60" height="60" />


## Before you start

Compatibility information
Vue does not support IE8 or earlier because it uses ECMAScript 5 functionality. But it supports all ECMAScript 5 compatible browsers

Release Notes
Latest stable version: v2.6.10

More release notes for each version are available on [GitHub](https://github.com/vuejs/vue/releases).


## Quick start

- [Download from Github](https://github.com/CAU-OSS-2019/team-project-team4/archive/master.zip).

- Clone the repo : `git clone https://github.com/CAU-OSS-2019/team-project-team4.git`.
- First, If you don't have node.js(to use npm) :  Downloal in here  https://nodejs.org/ko/
-  Second,  To use the npm module `npm install`
- Because of  using --global option  you need to use ` sudo`
install yarn :` sudo npm install --global yarn`

- We ned 3.x verserion, installing the official 3.x CLI : ` npm install -g @vue/cli`
- or if you installed yarn : `yarn global add @vue/cli`
-[Check vue version] : `vue --version`

- `npm run serve `or `yarn run serve `


## File Structure
Within the download you'll find the following directories and files:

```
|-- Vue Argon Dashboard
    |-- .gitignore
    |-- CHANGELOG.md
    |-- ISSUES_TEMPLATE.md
    |-- LICENSE.md
    |-- README.md
    |-- babel.config.js
    |-- package.json
    |--node-modules
    |-- public
    |   |-- favicon.ico
    |   |-- index.html
    |   |-- manifest.json
    |   |-- robots.txt
    |   |-- img
    |-- src
        |-- App.vue
        |-- main.js
        |-- registerServiceWorker.js
        |-- router.js
        |-- assets
        |   |-- logo.png
        |   |-- scss
        |   |   |-- argon.scss
        |   |-- vendor
        |       |-- @fortawesome
        |       |-- nucleo
        |-- components
        |   |-- Badge.vue
        |   |-- BaseAlert.vue
        |   |-- BaseButton.vue
        |   |-- BaseCheckbox.vue
        |   |-- BaseDropdown.vue
        |   |-- BaseHeader.vue
        |   |-- BaseInput.vue
        |   |-- BaseNav.vue
        |   |-- BasePagination.vue
        |   |-- BaseProgress.vue
        |   |-- BaseRadio.vue
        |   |-- BaseSlider.vue
        |   |-- BaseSwitch.vue
        |   |-- BaseTable.vue
        |   |-- Card.vue
        |   |-- CloseButton.vue
        |   |-- Modal.vue
        |   |-- NavbarToggleButton.vue
        |   |-- StatsCard.vue
        |   |-- stringUtils.js
        |   |-- Charts
        |   |   |-- BarChart.js
        |   |   |-- DoughnutChart.js
        |   |   |-- LineChart.js
        |   |   |-- PieChart.js
        |   |   |-- config.js
        |   |   |-- globalOptionsMixin.js
        |   |   |-- optionHelpers.js
        |   |-- SidebarPlugin
        |   |   |-- SideBar.vue
        |   |   |-- SidebarItem.vue
        |   |   |-- index.js
        |   |-- Tabs
        |       |-- PillsLayout.vue
        |       |-- Tab.vue
        |       |-- TabPane.vue
        |       |-- Tabs.vue
        |       |-- TabsLayout.vue
        |-- directives
        |   |-- click-ouside.js
        |-- layout
        |   |-- AuthLayout.vue
        |   |-- Content.vue
        |   |-- ContentFooter.vue
        |   |-- DashboardLayout.vue
        |   |-- DashboardNavbar.vue
        |-- plugins
        |   |-- argon-dashboard.js
        |   |-- globalComponents.js
        |   |-- globalDirectives.js
        |-- views
            |-- Dashboard.vue
            |-- Defalut.vue
            |-- Icons.vue
            |-- login_nouse.vue
            |-- Maps.vue
            |-- Register.vue
            |-- Tables.vue
            |-- UserProfile.vue
            |-- Dashboard
            |   |-- PageVisitsTable.vue
            |   |-- SocialTrafficTable.vue
            |-- Tables
                |-- ProjectsTable.vue
```


## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://github.com/creativetimofficial/public-assets/blob/master/logos/chrome-logo.png?raw=true" width="64" height="64"> <img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/firefox-logo.png" width="64" height="64"> <img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/edge-logo.png" width="64" height="64"> <img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/safari-logo.png" width="64" height="64"> <img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/opera-logo.png" width="64" height="64">



## Resources
- License Agreement: <https://www.creative-tim.com/license?ref=ada-github-readme>

- Issues: [Github Issues Page](https://github.com/CAU-OSS-2019/team-project-team4/issues?ref=ada-github-readme)

## Licensing

- Licensed under MIT (https://github.com/creativetimofficial/vue-argon-dashboard/blob/master/LICENSE.md)
- Copyright 2018 Creative Tim (https://www.creative-tim.com/?ref=ada-github-readme)

## Useful Links

- [How To Start Vue](https://kr.vuejs.org/v2/guide/index.html#Vue-js%EA%B0%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94)
- [Tutorials](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w?ref=creativetim)
- [Blog Creative Tim](http://blog.creative-tim.com/?ref=ada-github-readme)
