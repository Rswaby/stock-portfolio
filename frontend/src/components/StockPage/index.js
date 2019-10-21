import React, { Component } from 'react';
import axios from 'axios';
import { AuthUserContext } from '../Session';
import { Link } from 'react-router-dom';
const style = {
    link: {
      "textDecoration": "none",
      "color": "black",
      "textAlign": "center",
    }
  }

class StockPage extends Component {
    state = {
        symbol: '',
        loaded: '',
        data: {}
    }
    componentWillMount() {
        const { symbol } = this.props.match.params;
        this.setState({
            symbol: symbol
        })

        if (symbol) {
            this.fetchStockInfo(symbol)
        }

        console.log(this.props)
    }

    handlePurchase = () => {

    }

    fetchStockInfo = (symbol) => {

        axios.get(`/api/live/${symbol}/daily`)
            .then(res => {
                const data = res.data
                this.setState({
                    data: data
                })
            })

    }


    render() {
        const { symbol, data } = this.state;
        console.log(data.data)
        return (
            <div className={"m-top-50"}>
                <h5 className={"stock-title"}>{localStorage.getItem(symbol)}</h5>
                <div className={"stock-details-section m-left-5"}>
                    <div className={"stock-info-section"}>
                        <h6> Symbol : {symbol}</h6>
                        <br />
                        {data.data && (<div>
                            <p>Open   : ${data.data["1. open"]}</p>
                            <p>Close  : ${data.data["4. close"]}</p>
                            <p>High   : ${data.data["2. high"]}</p>
                            <p>Low    : ${data.data["3. low"]}</p>
                            <p>Volume : {data.data["5. volume"]}</p>
                        </div>
                        )}
                    </div>
                    <div className={"stock-purchase-or-login"}>
                        <AuthUserContext.Consumer>
                            {authUser =>
                                authUser ? (
                                    <div>purchase stock</div>
                                ) : (
                                    <Link  to={"/signin"}>SIGN IN</Link>
                                )

                            }
                        </AuthUserContext.Consumer>
                    </div>
                </div>
            </div>
        )
    }
}

export default StockPage;