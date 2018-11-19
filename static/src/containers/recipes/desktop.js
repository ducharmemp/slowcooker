import React, { PureComponent } from 'react';

import { Recipe } from '../../components/recipes';

class RecipeContainer extends PureComponent {
    render() {

        return (
            <Recipe recipeTitle='Bam spam fizz' />
        );
    }
}

export default RecipeContainer;
