import PropTypes from 'prop-types';
import React, { Component } from 'react';


class Recipe extends Component {
    static propTypes = {
        recipeTitle: PropTypes.string.isRequired
    }

    render () {
        const {
            recipeTitle
        } = this.props;
        return <div>{recipeTitle}</div>
    }
}

export default Recipe;
