import React, { Component } from 'react';

import { Card, Grid } from 'semantic-ui-react' ;

import { Recipe } from '../../components/recipes';

class RecipeContainer extends Component {
    componentDidMount() {
        this.props.loadGeneralRecipes();
    }

    render() {
        const {
            generalRecipes
        } = this.props;
        return (
            <Grid centered columns={2}>
                <Grid.Column>
                    <Card.Group>
                        {generalRecipes.map(element => {
                            const { name: recipeTitle, ingredients, pictures, steps, id } = element;
                            return <Recipe recipeTitle={recipeTitle} key={id} />
                        })}
                    </Card.Group>
                </Grid.Column>
                <Grid></Grid>
            </Grid>
        );
    }
}

export default RecipeContainer;
