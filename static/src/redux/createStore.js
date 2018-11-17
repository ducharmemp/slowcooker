import { createStore, applyMiddleware, combineReducers } from 'redux';
// import createLogger from 'redux-logger';
// import toDoApp from './modules/toDoApp';

// const loggerMiddleware = createLogger();

const createStoreWithMiddleware = applyMiddleware()(createStore);

const reducer = combineReducers({
});

const configureStore = (initialState) => createStoreWithMiddleware(reducer, initialState);
export default configureStore;
