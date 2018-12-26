import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { toPairs } from 'lodash';
import Dropzone from 'react-dropzone';
import { Form, Label, Button, List, Grid } from 'semantic-ui-react';
import injectSheet from 'react-jss';

function humanFileSize(size) {
    var i = Math.floor( Math.log(size) / Math.log(1024) );
    return ( size / Math.pow(1024, i) ).toFixed(2) * 1 + ' ' + ['B', 'kB', 'MB', 'GB', 'TB'][i];
};

const styles = {
    fileContainer: {
        overflow: 'auto',
        maxHeight: '10em'
    }
}


class RecipeForm extends Component {
    constructor() {
        super();
        this.state = {
            files: {}
        }
    }

    onDrop = (acceptedFiles) => {
        const { files: prevFiles } = this.state,
            files = {};

        Array.from(acceptedFiles).forEach((file) => {
            files[file.name] = file;
        })

        this.setState({files: {...prevFiles, ...files}});
    }

    render () {
        const { classes } = this.props;
        return (
        <Form>
            <Form.Field>
                <Grid columns={3}>
                    <Grid.Column>
                        <Dropzone onDrop={this.onDrop}>
                            <Label
                                as="label"
                                basic
                                htmlFor="upload"
                            >
                                Select file(s)
                            </Label>
                        </Dropzone>
                        </Grid.Column>
                    <Grid.Column>
                        <List divided relaxed verticalAlign='middle' className={classes.fileContainer}>
                            { toPairs(this.state.files).map(([fileName, fileObj]) => (
                                <List.Item key={fileName}>
                                    <List.Icon name='image' size='large' />
                                    <List.Content floated='right'>
                                        <Button>Remove</Button>
                                    </List.Content>
                                    <List.Content>
                                        <List.Header>
                                            {fileName}
                                        </List.Header>
                                        <List.Description>
                                            {humanFileSize(fileObj.size)}
                                        </List.Description>
                                    </List.Content>
                                </List.Item>
                            )) }
                        </List>
                    </Grid.Column>
                </Grid>
            </Form.Field>
            <Button type='submit'>Submit</Button>
        </Form>);
    }
}

export default injectSheet(styles)(RecipeForm);
