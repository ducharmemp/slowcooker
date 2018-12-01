import * as axios from 'axios';
import { put, takeEvery, call } from 'redux-saga/effects';

import history from '../../history';

const USER_AUTHENTICATION = 'USER_AUTHENTICATION',
    USER_AUTHENTICATION_LOADING = 'USER_AUTHENTICATION_LOADING',
    USER_AUTHENTICATION_SUCCESS = 'USER_AUTHENTICATION_SUCCESS',
    USER_AUTHENTICATION_ERROR = 'USER_AUTHENTICATION_ERROR',
    USER_LOGOUT = 'USER_LOGOUT';

const storedUser = window.localStorage.getItem('session');

const initialState = {
    error: false,
    loading: false,
    properties: (storedUser && decodeJWT(storedUser)) || {}
};

function decodeJWT(tok) {
    const base64 = tok.split('.')[1].replace('-', '+').replace('_', '/');
    return JSON.parse(window.atob(base64));
}

export const authenticateUserAction = (username, password) => ({
    type: USER_AUTHENTICATION,
    payload: { username, password }
});

export const logoutUserAction = () => ({
    type: USER_LOGOUT,
    error: false,
    loading: false
})

const authenticateUserSuccess = (user, token) => ({
    type: USER_AUTHENTICATION_SUCCESS,
    payload: user,
    error: false,
    loading: false,
    token
})

const authenticateUserError = err => ({
    type: USER_AUTHENTICATION_ERROR,
    payload: err,
    error: true,
    loading: false
})

const authenticateUserLoading = () => ({
    type: USER_AUTHENTICATION_LOADING,
    error: false,
    loading: true
})

function* _authenticateUser(action) {
    yield put(authenticateUserLoading())
    try {
        const response = yield call(axios.post, '/api/v1/users/login', {name: action.payload.username, password: action.payload.password});
        yield put(authenticateUserSuccess(decodeJWT(response.data.token), response.data.token));
        history.goBack();
    } catch (error) {
        window.localStorage.removeItem('session');
        yield put(authenticateUserError(error));
    }
}

export function* watchAuthenticationAsync() {
    yield takeEvery(USER_AUTHENTICATION, _authenticateUser);
}

export default function reducer(state = initialState, action) {
  switch (action.type){
  case USER_AUTHENTICATION_LOADING:
    return {...state, error: action.error};
  case USER_AUTHENTICATION_SUCCESS:
    window.localStorage.setItem('session', action.token);
    return {...state, properties: action.payload};
  case USER_AUTHENTICATION_ERROR:
  case USER_LOGOUT:
    window.localStorage.removeItem('session');
    return {...initialState, error: action.error};
  default:
    return state;
  }
}
