import React, { Component } from 'react';
// import { AuthUserContext } from '../Session';



class StockPage extends Component {
    state = {
        symbol: ''
    }
    componentWillMount() {
        const { symbol } = this.props.match.params;
        this.setState({
            symbol: symbol
        })
        console.log(this.props)
    }


    render() {
        const { symbol } = this.state;
        return (
            <div className={"stock-detail-wrapper"}>
                <div className={"stock-title"}>{localStorage.getItem(symbol)}</div>
                <div className={"stock-details-section m-left-5"}>
                    <div className={"stock-info-section"}>
                        Stock-detail
                    </div>
                    <div className={"stock-purchase-or-login"}>
                        Login or purchase Stock section
                    </div>
                </div>
            </div>
        )
    }
}

export default StockPage;