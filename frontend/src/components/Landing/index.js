import React, { Component } from 'react';
import axios from 'axios';
import StockCard from "../StockCard/index";
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
        <div className={"card-result-area"}>
          {this.state.loaded &&
            this.state.data.map((ticker, index) =>
              <StockCard key={index} data={ticker} />
            )}
        </div>
      </div>
    )
  }
}
export default Landing;
