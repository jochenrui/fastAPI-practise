import "./RankedStatsCard.css";
import { RankedStats } from "../../types";

type Props = {
    rankedStats: RankedStats
}

const RankedStatsCard = ({rankedStats}
    :Props) => {

        const {
            leagueId, queueType, tier, rank, summonerId, summonerName, leaguePoints, wins, losses, veteran, inactive, freshBlood, hotStreak} = rankedStats;

    return(
        <div className="ranked-stats-box">
            <h1>Season 11 Ranked Stats</h1>
            <p>Summoner: {summonerName}</p>
            <p>Rank: {tier + " " + rank}</p>
            <p>Wins: {wins}</p>
            <p>Losses: {losses}</p>
        </div>
    )
}

export default RankedStatsCard;