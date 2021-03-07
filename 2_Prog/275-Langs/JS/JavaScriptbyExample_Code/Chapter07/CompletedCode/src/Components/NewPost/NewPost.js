import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';
import uuidv4 from 'uuid/v4';

import apiCall from '../../services/api/apiCall';
import ErrorMessage from '../Common/ErrorMessage';
import SuccessMessage from '../Common/SuccessMessage';
import LoadingIndicator from '../Common/LoadingIndicator';
import PostInputField from './Components/PostInputField';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as postActions from '../../redux/actions/postActions';

class NewPost extends Component {

  static propTypes = {
    postActions: PropTypes.object.isRequired,
    loading: PropTypes.bool.isRequired,
    hasError: PropTypes.bool.isRequired,
  }

  constructor() {
    super();

    this.state = {
      author: '',
      title: '',
      content: '',
      noOfLines: 0,
      success: false,
    };
    this.editAuthorName = this.editAuthorName.bind(this);
    this.editContent = this.editContent.bind(this);
    this.editTitle = this.editTitle.bind(this);
    this.submit = this.submit.bind(this);
  }

  submit() {
    if(this.state.author && this.state.content && this.state.title) {
      this.setState({loading: true});

      const date = new Date();
      const epoch = (date.getTime()/1000).toFixed(0).toString();
      const body = {
        id: uuidv4(),
        author: this.state.author,
        title: this.state.title,
        content: this.state.content,
        datetime: epoch,
      };

      this.props.postActions.addNewPost(body);

    } else {
      alert('Please Fill in all the fields');
    }
  }

  editAuthorName(event) {
    this.setState({author: event.target.value});
  }

  editContent(event) {
    const linesArray = event.target.value.split('\n');
    this.setState({content: event.target.value, noOfLines: linesArray.length});
  }

  editTitle(event) {
    this.setState({title: event.target.value});
  }

  componentWillReceiveProps(nextProps) {
    if(this.props !== nextProps) {
      if(nextProps.loading === false && nextProps.hasError === false) {
        this.setState({
          success: true,
          author: '',
          title: '',
          content: '',
        });
      } else if(nextProps.loading === false && nextProps.hasError === true) {
        this.setState({success: false});
      }
    }
  }

  render() {

    const noOfLines = this.state.noOfLines < 5 ? 5 : this.state.noOfLines;

    return(
      <div className={'container'}>
        <h2>Write Post</h2>

        <PostInputField
          className={'author-name-input'}
          id={'author'}
          title={'Author Name:'}
          value={this.state.author}
          onChange={this.editAuthorName}
        />

        <PostInputField
          className={'title-input'}
          id={'title'}
          title={'Title:'}
          value={this.state.title}
          onChange={this.editTitle}
        />

        <div className="form-group content-text-area">
          <label htmlFor="content">Post:</label>
          <textarea className="form-control" rows={noOfLines} id="content" value={this.state.content} onChange={this.editContent}></textarea>
        </div>

        {
          this.props.loading
          ?
            <LoadingIndicator />
          :
            <button type="button" className="btn btn-primary" onClick={this.submit}>Submit Post</button>
        }

        {
          this.props.hasError
          ?
            <ErrorMessage title={'Error!'} message={`Unable to submit post!`} />
          :
            null
        }

        {
          this.state.success
          ?
            <SuccessMessage title={'Success!'} message={`Post has been Submitted!`} />
          :
            null
        }

      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    loading: state.ajaxCalls.addPost.loading,
    hasError: state.ajaxCalls.addPost.hasError,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    postActions: bindActionCreators(postActions, dispatch),
  };
}
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(NewPost);
