import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

import { loadGeneralRecipesAction, loadUserRecipesAction } from '../../store/modules/recipes';

import DesktopContainer from './desktop';
// import MobileContainer from './mobile';


const ResponsiveContainer = (props) => {
    console.log(props)
    return (
        <div>
            <DesktopContainer loadGeneralRecipes={props.loadGeneralRecipes} generalRecipes={props.generalRecipes}>{props.children}</DesktopContainer>
            {/* <MobileContainer>{children}</MobileContainer> */}
        </div>
    );
}

    ResponsiveContainer.propTypes = {
    children: PropTypes.node,
}

function mapStateToProps(state) {
    console.log(state)
    return {
        generalRecipes: state.recipes.generalRecipes.list
    };
}

function mapDispatchToProps(dispatch) {
    return {
        loadGeneralRecipes: (page) => dispatch(loadGeneralRecipesAction(page)),
        loadUserRecipes: (user) => dispatch(loadUserRecipesAction(user))
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(ResponsiveContainer);
