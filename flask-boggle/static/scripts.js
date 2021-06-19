/* === Global Variables === */
const $FORM = $('#user-form');
const $INPUT = $('#user-input');
const $ALERTS = $('#alert-container');
const $SCORE = $('#score');
const $START = $('#start');
const $TIMER = $('#timer');
const VAL_GUESSES = [];

// --------------------------

class BoggleBoard {
  /* Control all game logic and interactions on the gameboard */
  constructor(board, seconds = 60) {
    this.seconds = seconds;
    this.score = 0;
    this.words = new Set();
    this.$board = $("#" + board)
  }
}

const buildHtmlAlert = (message) => {
  $alert = $('<div>').

    return
}

const startGame = () => {
  // TODO: Add Functionality
}

/** 
 * endGame is triggered when the game timer hits 0, which will prevent new
 * form submissions & toggle the end-game modal. 
 */
const endGame = () => {
  $FORM.children('button').prop('disabled', 'true');
  $INPUT.prop('disabled', 'true');
}

/** 
 * 
 */
const restartGame = () => {
  // TODO: Add Functionailty
}

/** 
 * Calculates and updates current game score based on VAL_GUESSES
 */
const updateScore = () => {
  let newScore = 0;

  VAL_GUESSES.map((word) => {
    console.log(word)
    newScore = word.length + newScore;
  })

  $SCORE.text(newScore)
}

/**
 * Displays guess feedback from the users submission/
 */
const updateGuessStatus = (result, guess) => {
  userMessages = {
    "ok": `"${guess}" is valid, nice work!`,
    "not-word": `"${guess}" is not a valid word. Try again.`,
    "not-on-board": `"${guess}" cannot be formed on the board, Try Again.`,
  }

  message = userMessages[result]

  // Todo: Build Fancy Alert to Inject into the Page.
  // Todo: Figure out how to have alert slowly disappear.  
  $ALERTS.append(message)
}

// COUNT DOWN TIMER 
$(document).ready(() => {
  // Each round = 3 minutes
  seconds = 60;

  const intervalId = setInterval(() => {
    currTime = $TIMER.text();
    newTime = currTime - 1;

    if (newTime == '0') {
      clearInterval(intervalId)
      endGame()
    }
    $TIMER.text(newTime)
  }, 1000)
})

/* === EVENT HANDLERS === */
$FORM.submit('click', async (e) => {
  e.preventDefault();
  const guess = $INPUT.val().toLowerCase().trim();

  // // Todo: Remove comments once compelted. 
  // if (VAL_GUESSES.indexOf(guess) > -1) {
  //   console.log("Guess already made");
  //   // Todo: Notify user of duplicate guess. 
  // }
  const resp = await axios.post('/validate-guess', { guess }).then((resp) => {
    const result = resp.data['result'];
    if (result === "ok") {
      VAL_GUESSES.push(guess);
      updateScore();
    }

    // Todo: Trigger message to the user. 
    updateGuessStatus(result, guess)
  })
})