import React from 'react';

const StockCard = ({data}) => (
    <div className={"card"}>
        <div className={"content"}>{data["1. symbol"]}</div>
    </div>
)

export default StockCard;

// {
//     "ticker": {
//       "1. symbol": "MSFT",
//       "2. name": "Microsoft Corporation",
//       "3. type": "Equity",
//       "4. region": "United States",
//       "5. marketOpen": "09:30",
//       "6. marketClose": "16:00",
//       "7. timezone": "UTC-04",
//       "8. currency": "USD",
//       "9. matchScore": "1.0000"
//     }
//   }