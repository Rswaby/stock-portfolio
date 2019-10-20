import React, { Component } from 'react';
import axios from 'axios';
const Landing = () => (<Search />);

class Search extends Component {
  state = {
    keyword: '',
    loaded: false,
    data: []
  }

  fetchInfo = () => {
    axios.get(`/api/live/${this.state.keyword}`)
      .then(res => {
        const data = res.data
        this.setState({
          loaded: true,
          data: data
        })
      })
  }


  handleInputChange = () => {
    this.setState({
      keyword: this.search.value
    })
  }

  handleOnSubmit = (event) => {
    console.log(this.state.keyword)
    this.fetchInfo()
    event.preventDefault()
  }

  render() {
    console.log(this.state)
    return (
      <div className={"searchPage m-top-5"}>
        <h4 className={"centr"}>Browse Stocks</h4>
        <form className={"search"} onSubmit={this.handleOnSubmit}>
          <input
            className={"searchTerm"}
            placeholder="search..."
            ref={input => this.search = input}
            onChange={this.handleInputChange}
          />
        </form>
        {/* {this.state.loaded ? <p>{this.state.data}</p> : null} */}
        <p>Cards go here</p>
      </div>
    )
  }
}
export default Landing;
