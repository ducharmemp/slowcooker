import * as axios from 'axios';
import { combineReducers } from 'redux';
import { put, takeEvery, call } from 'redux-saga/effects';

const LOAD_GENERAL_RECIPES = 'LOAD_GENERAL_RECIPES',
    LOAD_GENERAL_RECIPES_LOADING = 'LOAD_GENERAL_RECIPES_LOADING',
    LOAD_GENERAL_RECIPES_SUCCESS = 'LOAD_GENERAL_RECIPES_SUCCESS',
    LOAD_GENERAL_RECIPES_ERROR = 'LOAD_GENERAL_RECIPES_ERROR',
    LOAD_USER_RECIPES = 'LOAD_USER_RECIPES',
    LOAD_USER_RECIPES_LOADING = 'LOAD_USER_RECIPES_LOADING',
    LOAD_USER_RECIPES_SUCCESS = 'LOAD_USER_RECIPES_SUCCESS',
    LOAD_USER_RECIPES_ERROR = 'LOAD_USER_RECIPES_ERROR';

const generalRecipesInitialState = {
    error: false,
    loading: false,
    list: []
};

const userRecipesInitialState = {
    error: false,
    loading: false,
    list: []
}

export const loadGeneralRecipesAction = (page=1) => {
    return {
        type: LOAD_GENERAL_RECIPES,
        payload: { page }
    }
}

const loadGeneralRecipesSuccess = (recipes) => ({
    type: LOAD_GENERAL_RECIPES_SUCCESS,
    list: recipes,
    error: false,
    loading: false
})

const loadGeneralRecipesError = err => ({
    type: LOAD_GENERAL_RECIPES_ERROR,
    payload: err,
    error: true,
    loading: false
})

const loadGeneralRecipesLoading = () => ({
    type: LOAD_GENERAL_RECIPES_LOADING,
    error: false,
    loading: true
})

function* _loadGeneralRecipes(action) {
    yield put(loadGeneralRecipesLoading());
    try {
        const res = yield axios.get('/api/v1/recipes');
        yield put(loadGeneralRecipesSuccess(res.data));
    } catch (err) {
        yield put(loadGeneralRecipesError(err));
    }
}

export const loadUserRecipesAction = (user) => {
    return {
        type: LOAD_USER_RECIPES,
        payload: user
    }
}

const loadUserRecipesSuccess = (recipes) => ({
    type: LOAD_USER_RECIPES_SUCCESS,
    list: recipes,
    error: false,
    loading: false
})

const loadUserRecipesError = err => ({
    type: LOAD_USER_RECIPES_ERROR,
    payload: err,
    error: true,
    loading: false
})

const loadUserRecipesLoading = () => ({
    type: LOAD_USER_RECIPES_LOADING,
    error: false,
    loading: true
})

function* _loadUserRecipes(action) {
    yield put(loadUserRecipesLoading());
    try {
        const res = yield axios.get(`/api/v1/users/${action.payload.user.id}/recipes`);
        yield put(loadUserRecipesSuccess(res));
    } catch (err) {
        yield put(loadUserRecipesError(err));
    }
}

export function* watchRecipesAsync() {
    yield takeEvery(LOAD_GENERAL_RECIPES, _loadGeneralRecipes);
    yield takeEvery(LOAD_USER_RECIPES, _loadUserRecipes);
}

function generalRecipes(state = generalRecipesInitialState, action) {
    switch (action.type){
    case LOAD_GENERAL_RECIPES_LOADING:
        return {...state, error: action.error, loading: action.loading};
    case LOAD_GENERAL_RECIPES_SUCCESS:
        return {...state, list: action.list};
    case LOAD_GENERAL_RECIPES_ERROR:
        return {...state, error: action.error};
    default:
        return state;
    }
}

function userRecipes(state = userRecipesInitialState, action) {
    switch (action.type){
    case LOAD_USER_RECIPES_LOADING:
        return {...userRecipesInitialState};
    case LOAD_USER_RECIPES_SUCCESS:
        return {...userRecipesInitialState};
    case LOAD_USER_RECIPES_ERROR:
        return {...userRecipesInitialState};
    default:
        return state;
    }
}

export default combineReducers({
    generalRecipes,
    userRecipes
})
