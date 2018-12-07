import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {Router, Route, Switch} from 'react-router-dom';
import 'semantic-ui-css/semantic.min.css';

import './styles/fonts.css';
import history from './history';

import {
    HomepageLayout,
    RecipeLayout,
    LoginLayout,
    NotFoundLayout
 } from './containers';
import store from './store/createStore';
import * as serviceWorker from './serviceWorker';

ReactDOM.render((
    <Provider store={store}>
        <Router history={history}>
            <Switch>
                <Route exact path='/' component={HomepageLayout} />
                <Route exact path='/recipes' component={RecipeLayout} />
                <Route exact path='/login' component={LoginLayout} />
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
