import PropTypes from 'prop-types'
import React, { Component } from 'react'
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import {
  Button,
  Container,
  Menu,
  Responsive,
  Segment,
  Visibility,
} from 'semantic-ui-react';
import { isEmpty } from 'lodash';

import { HomepageHeading } from '../../components/home';

class DesktopContainer extends Component {
    state = {}

    hideFixedMenu = () => this.setState({ fixed: false })
    showFixedMenu = () => this.setState({ fixed: true })

    renderAuthentication(fixed, authenticationFunc) {
        return (<Menu.Item position='right'>
            <Link to='/login'>
          <Button as='a' inverted={!fixed} onClick={authenticationFunc}>
              Log in
          </Button>
          </Link>
          <Link to='/login'>
          <Button as='a' inverted={!fixed} primary={fixed} style={{ marginLeft: '0.5em' }}>
              Sign Up
          </Button>
          </Link>
        </Menu.Item>);
    }

    render() {
      const {
          children,
          authenticateUser,
          user
        } = this.props;
      const { fixed } = this.state;

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
                  { isEmpty(user) && this.renderAuthentication(fixed, authenticateUser) }
                </Container>
              </Menu>
              <HomepageHeading />
            </Segment>
          </Visibility>

          {children}
        </Responsive>
      )
    }
  }

  function mapStateToProps(state, ownProps) {
      return {};
  }

  function mapDispatchToProps(dispatch) {
}

DesktopContainer.defaultProps = {
    user: {}
}

DesktopContainer.propTypes = {
    children: PropTypes.node,
    user: PropTypes.object
}

export default connect(mapStateToProps, mapDispatchToProps)(DesktopContainer);
