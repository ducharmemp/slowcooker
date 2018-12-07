import PropTypes from 'prop-types';
import React, { Component } from 'react';

import { Card, Image } from 'semantic-ui-react';


class Recipe extends Component {
    static propTypes = {
        recipeTitle: PropTypes.string.isRequired
    }

    render () {
        const {
            recipeTitle,
            recipeDescription
        } = this.props;
        return (
        <Card>
            <Image src='/404.png' size='big' />
            <Card.Content>
                <Card.Header>
                    {recipeTitle}
                </Card.Header>
                <Card.Description>
                    {recipeDescription}
                </Card.Description>
            </Card.Content>
        </Card>);
    }
}

export default Recipe;
