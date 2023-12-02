import fs from 'fs';
import readline from 'readline';

const filePath = 'input.txt';

let validGame = new Map([['red', 12], ['green', 13], ['blue', 14]])

let rt = 0

let rt2 = 0

const rl = readline.createInterface({
    input: fs.createReadStream(filePath),
    output: process.stdout,
    terminal: false
});
  
// New line event
rl.on('line', (line) => {
    let id = findID(line)
    let games = getGames(line)
    if(isValidGame(games)){
        rt += id
    }

    rt2 += isValidGame(games)
});
  
//Close file event
rl.on('close', () => {
    console.log("Sum of valid games: ", rt)
    console.log("Sum of mininum valid games cubes: ", rt2)
});

function findID(line){
    let idStringGame = parseInt(line.split(":")[0].split(" ")[1])

    return idStringGame
}

function getGames(line){
    let games = line.split(":")[1].split(";")

    return games
}

function isValidGame(games){
    let isValid = true
    let minimumValidGame = new Map([['red', -1], ['green', -1], ['blue', -1]])
    games.forEach((game) =>{
         let cubes = game.trim().split(",")

        cubes.forEach((e) =>{
            let hand = e.trim().split(" ")
            let color = hand[1]
            let number = parseInt(hand[0])

            minimumValidGame.get(color) < number || minimumValidGame.get(color) == -1 ? minimumValidGame.set(color, number) : ""

            validGame.forEach((value, key) => {
                if(key == color){
                    if(value < number){
                        isValid = false
                        return isValid
                    }
                }
            })
        })  
    })

    let rt = 1
    minimumValidGame.forEach((value, key) => {
        rt = rt * value
    })
    
    return isValid, rt
}