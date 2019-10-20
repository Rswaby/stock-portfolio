import React, { Component } from 'react';
// import { AuthUserContext } from '../Session';



class StockPage extends Component {

    componentWillMount() {
        console.log(this.props)
    }
    render() {
        return (
            <div className={"stock-detail-wrapper"}>
                <div className={"stock-title"}>Stock-title-page</div>
                <div className={"stock-details-section"}>
                    <div className={"stock-info-section"}>Stock-detail</div>
                    <div className={"stock-purchase-or-login"}> Login or purchase Stock section</div>
                </div>
            </div>
        )
    }
}

export default StockPage;