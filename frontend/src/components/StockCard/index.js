import React from 'react';
import { Link } from 'react-router-dom';

const StockCard = ({ data }) => (
    <Link to={'#'}>
        <div className={"card"}>

            <div className={"content"}>
                <h6> {data["1. symbol"]}</h6>
                <p>{data["2. name"]}</p>
                <br />
                <p>Market Open | {data["5. marketOpen"]} </p>
                <p>Market Close | {data["6. marketClose"]}</p>
                <p>Currency | {data["8. currency"]} </p>
            </div>

        </div>
    </Link>
)

export default StockCard;