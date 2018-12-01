import React from 'react';
import { connect } from 'react-redux';
import { Form } from 'semantic-ui-react';

import { authenticateUserAction } from '../../store/modules/user';

class LoginContainer extends React.Component {
    constructor() {
        super();
        this.state = {
            username: '',
            password: ''
        }
    }

    handleChange = (property) => (event) => {
        event.preventDefault();
        this.setState({[property]: event.target.value});
    }

    handleSubmit = () => {
        const { authenticateUser } = this.props;
        authenticateUser(this.state.username, this.state.password);
    }

    render() {
        const {
            loading
        } = this.props;
        return (
            <div>
                <Form loading={loading}>
                    <Form.Input label="Username" placeholder="User Name" onChange={this.handleChange('username')} />
                    <Form.Input label="Password" placeholder="Password" type="password" onChange={this.handleChange('password')} />
                    <Form.Button onClick={this.handleSubmit}></Form.Button>
                </Form>
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {
        user: state.user.properties,
        loading: state.user.loading
    };
}

function mapDispatchToProps(dispatch) {
    return {
        authenticateUser: (user, password) => dispatch(authenticateUserAction(user, password))
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(LoginContainer);
