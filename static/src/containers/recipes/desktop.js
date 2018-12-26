import React, { Component } from 'react';
import { Card, Grid } from 'semantic-ui-react' ;
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

import { RecipeCard, RecipeForm } from '../../components/recipes';

class RecipeContainer extends Component {
    componentDidMount() {
        this.props.loadGeneralRecipes();
    }

    render() {
        const {
            generalRecipes
        } = this.props;
        return (
            <div>
                <Grid centered columns={2}>
                    <Grid.Column>
                        <Slider autoplay dots fade infinite speed={2000}>
                            {generalRecipes.map(element => {
                                const { name: recipeTitle, ingredients, pictures, steps, id } = element;
                                return <RecipeCard recipeTitle={recipeTitle} key={id} pictures={pictures} />
                            })}
                        </Slider>
                    </Grid.Column>
                </Grid>
                <RecipeForm />
            </div>
        );
    }
}

export default RecipeContainer;
