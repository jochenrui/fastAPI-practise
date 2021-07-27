import { useEffect, useState } from "react"
import { RankedStatsCard } from "../../components"
import { RankedStats } from "../../types"

const RankedStatsPage = () => {

    const [rankedStats, setRankedStats] = useState<RankedStats | undefined>(undefined)


    useEffect(() => {
        fetch("http://localhost:8080/ranked-stats/volx2")
        .then(response => response.json())
        .then(data => {
            let rankedStatsResult = data[0];
            setRankedStats(rankedStatsResult);
        })
        .catch(err => console.log(err))
    }, [])

    return(
        <>
            {rankedStats !== undefined && <RankedStatsCard rankedStats={rankedStats}/>}
            
        </>
    )
}

export default RankedStatsPage
