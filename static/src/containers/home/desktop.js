import PropTypes from 'prop-types'
import React, { Component, Fragment } from 'react'
import { Link } from 'react-router-dom';
import {
  Button,
  Container,
  Menu,
  Responsive,
  Segment,
  Visibility,
  Icon
} from 'semantic-ui-react';
import { isEmpty } from 'lodash';

import { HomepageHeading } from '../../components/home';

class DesktopContainer extends Component {
    state = {}

    hideFixedMenu = () => this.setState({ fixed: false })
    showFixedMenu = () => this.setState({ fixed: true })

    renderAuthentication(fixed, loginCallback, setupCallback) {
        return (
            <Fragment>
            <Button as='a' inverted={!fixed} onClick={loginCallback}>
                Log in
            </Button>
            <Button as='a' inverted={!fixed} primary={fixed} style={{ marginLeft: '0.5em' }} onClick={setupCallback}>
                Sign Up
            </Button>
        </Fragment>);
    }

    render() {
    const {
            children,
            loginCallback,
            setupCallback,
            logoutUserCallback,
            user
        } = this.props,
        { fixed } = this.state,
        noUser = isEmpty(user);


    return (
        <Responsive minWidth={Responsive.onlyTablet.minWidth}>
            <Visibility
                once={false}
                onBottomPassed={this.showFixedMenu}
                onBottomPassedReverse={this.hideFixedMenu}
            >
                <Segment
                inverted
                textAlign='center'
                style={{ minHeight: 700, padding: '1em 0em' }}
                vertical
                >
                <Menu
                    fixed={fixed ? 'top' : null}
                    inverted={!fixed}
                    pointing={!fixed}
                    secondary={!fixed}
                    size='large'
                >
                    <Container>
                        <Menu.Item as='a' active>
                            Home
                        </Menu.Item>
                        <Menu.Item as='a'>Work</Menu.Item>
                        <Menu.Item as='a'>Company</Menu.Item>
                        <Menu.Item as='a'>Careers</Menu.Item>
                        <Menu.Item position='right'>
                            { noUser && this.renderAuthentication(fixed, loginCallback, setupCallback) }
                            { !noUser &&
                                <Fragment>
                                    <Link to='/profile'>
                                        <Icon name='user'/>
                                        { user.name }
                                    </Link>
                                    <Button inverted={!fixed} onClick={logoutUserCallback}>
                                        Log Out
                                    </Button>
                                </Fragment>
                            }
                        </Menu.Item>
                    </Container>
                </Menu>
                <HomepageHeading />
                </Segment>
            </Visibility>
            {children}
        </Responsive>)
    }
}

DesktopContainer.propTypes = {
    children: PropTypes.node,
    user: PropTypes.object
}

export default DesktopContainer;
