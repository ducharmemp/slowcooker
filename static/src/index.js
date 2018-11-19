import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import 'semantic-ui-css/semantic.min.css';

import './index.css';

import {
    HomepageLayout,
    RecipeLayout,
    NotFoundLayout
 } from './containers';
import configureStore from './store/createStore';
import * as serviceWorker from './serviceWorker';

ReactDOM.render((
    <Provider store={configureStore()}>
    <Router>
        <Switch>
            <Route exact path='/' component={HomepageLayout} />
            <Route exact path='/recipe' component={RecipeLayout} />
            <Route path='*' component={NotFoundLayout} />
        </Switch>
    </Router>
    </Provider>
    ),
    document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
