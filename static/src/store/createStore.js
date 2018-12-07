import { createStore, applyMiddleware, combineReducers, compose } from 'redux';
import createSagaMiddleware from 'redux-saga'
import { all } from 'redux-saga/effects'
// import createLogger from 'redux-logger';
// import toDoApp from './modules/toDoApp';
import user, { watchAuthenticationAsync } from './modules/user';
import recipes, { watchRecipesAsync } from './modules/recipes'

// const loggerMiddleware = createLogger();
const sagaMiddleware = createSagaMiddleware();
function* rootSaga() {
    yield all([
        watchAuthenticationAsync(),
        watchRecipesAsync(),
    ])
}

const reducer = combineReducers({
    user,
    recipes
});

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
    reducer,
    composeEnhancers(applyMiddleware(sagaMiddleware)),
)

sagaMiddleware.run(rootSaga);
export default store;
