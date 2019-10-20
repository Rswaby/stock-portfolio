import React from 'react';

const StockCard = ({ data }) => (
    <div className={"card"}>
        <div className={"content"}>
           <h6> {data["1. symbol"]}</h6>
           <p>{data["2. name"]}</p>
        </div>
    </div>
)

export default StockCard;