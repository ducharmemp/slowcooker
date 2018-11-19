import PropTypes from 'prop-types'
import React from 'react'
import {
  Button,
  Container,
  Header,
  Icon,
} from 'semantic-ui-react'
import styled from 'styled-components'

const CompanyTitle = styled(Header)`
    &&& {
        font-weight: normal;
        margin-bottom: 0;
        margin-top: 3em;
    }
`;


const HomepageHeading = ({ mobile }) => (
    <Container text>
      <CompanyTitle
        as='h1'
        content='Imagine-a-Company'
        inverted
        // style={{
        //   fontSize: mobile ? '2em' : '4em',
        //   fontWeight: 'normal',
        //   marginBottom: 0,
        //   marginTop: mobile ? '1.5em' : '3em',
        // }}
      />
      <Header
        as='h2'
        content='Do whatever you want when you want to.'
        inverted
        style={{
          fontSize: mobile ? '1.5em' : '1.7em',
          fontWeight: 'normal',
          marginTop: mobile ? '0.5em' : '1.5em',
        }}
      />
      <Button primary size='huge'>
        Get Started
        <Icon name='right arrow' />
      </Button>
    </Container>
  )
  
  HomepageHeading.propTypes = {
    mobile: PropTypes.bool,
  }
  
  export default HomepageHeading;
