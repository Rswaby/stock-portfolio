import React,{Component} from 'react';
import axios from 'axios';
const Landing = () => (
  <div>
    <h1><Search /></h1>
  </div>
);

class Search extends Component {
  state = {
    keyword: '',
    data: []
  }
//http://localhost:8000/api/live/MSFT
  fetchInfo = () => {
    axios.get(`http://localhost:8000/api/live/${this.state.keyword}`)
      .then(({ data }) => {
        this.setState({
          data: data.data
        },() => {
          
          if(this.state.keyword && this.state.keyword.length>2){
          
            //this.fetchInfo() 
          }
        })
      })
  }

  handleInputChange = () => {
    this.setState({
      keyword: this.search.value
    })
  }

  handleOnSubmit=(event)=>{
    console.log(this.state.keyword)
    this.fetchInfo()
    event.preventDefault()
  }

  render() {
    return (
      <form onSubmit={this.handleOnSubmit}>
        <input
          placeholder="seach stocks here"
          ref={input => this.search = input}
          onChange={this.handleInputChange}
        />
        <p>{this.state.data}</p>
      </form>
    )
  }
}
export default Landing;
