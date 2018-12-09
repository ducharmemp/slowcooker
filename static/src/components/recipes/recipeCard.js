import PropTypes from 'prop-types';
import React, { Component } from 'react';

import { Card, Image, Segment } from 'semantic-ui-react';


class RecipeCard extends Component {
    static propTypes = {
        recipeTitle: PropTypes.string.isRequired,
        recipePictureUrl: PropTypes.string.isRequired
    }

    static defaultProps = {
        recipePictureUrl: '/404.png'
    }

    render () {
        const {
            recipeTitle,
            recipeDescription,
            recipePictureUrl
        } = this.props;
        return (
        <Card fluid>
            <Image src={recipePictureUrl} size='big' centered/>
            <Card.Content>
                <Card.Header>
                    <Segment basic textAlign='center'>
                        {recipeTitle}
                    </Segment>
                </Card.Header>
                <Card.Description>
                    {recipeDescription}
                </Card.Description>
            </Card.Content>
        </Card>);
    }
}

export default Recipe;
