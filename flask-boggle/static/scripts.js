const UiManager = {
  /* === DOM Selectors === */
  $board: $('#board'),
  $form: $('#user-form'),
  $input: $('#user-input'),
  $score: $('#score'),
  $timer: $('#timer'),
  $wordList: $("#word-list"),
  $alert: $("#alert"),
  /* --------------------- */
  /**
   * Update the score within the UI.
   * @param {(string|number)} score test score to place on the page.
   */
  updateScore: function (score) {
    this.$score.text(score);
  },
  /**
   * Update timer within the UI. 
   * @param {(string|number)} time 
   */
  updateTimer: function (time) {
    this.$timer.text(time);
  },
  /**
   * Update wordlist within the UI for valid words found. 
   * @param {string} word word to add to #word-list
   */
  updateWordList: function (word) {
    const $li = $("<li>").text(word)
    this.$wordList.append($li);
  },
  /**
   * Reset the #form and focus on the #user-input.
   */
  resetForm: function () {
    this.$form.trigger('reset')
    this.$input.focus();
  },
  /**
   * Display a message to the user based on the results of their submission.
   * @param {string} message The specific message that will be displayed to the user.
   * @param {string} type The type of message, either success or error. 
   */
  displayMessage: function (message, type) {
    // Todo: add feat - spice up alert message
    this.$alert.removeClass('alert-success', 'alert-warning');

    if (type == 'success') {
      this.$alert.addClass('alert-success');
    } else if (type == 'error') {
      this.$alert.addClass('alert-warning');
    }
    // Display Message
    this.$alert.text(message);
    this.$alert.slideToggle()

    // Hide message momentarily after display.
    setTimeout(() => {
      this.$alert.slideToggle();
    }, 1500)
  },
  disableForm: function () {
    // Todo: add feat - disable 
    this.$input.prop("disabled", true)
    $("form > button").prop("disabled", true) // Todo: Check for alternative 

  },
  endGameModal: function (resp) {
    // Todo: add feat - end game modal

  }
}

class BoggleGame {
  /* Control all game logic and handle server interactions */
  constructor(seconds = 60) {
    this.seconds = seconds;
    this.score = 0;
    this.words = new Set();
    this.$board = UiManager.$board;

    // Link Form submit to class guess handler
    UiManager.$form.on("submit", this.guessHandler.bind(this));

    // Start Game Countdown
    this.timer = setInterval(this.countdown.bind(this), 1000)
  }

  async guessHandler(event) {
    event.preventDefault();
    const guess = $("#user-input").val().toLowerCase().trim();

    if (this.words.has(guess)) {
      UiManager.displayMessage(`"${guess}" was already found.`, 'error')
      return
    }

    const resp = await axios.post('/validate-guess', { guess })
    const result = resp.data['result'];
    const message = this._buildMessage(result, guess);

    if (result === 'ok') {
      this.words.add(guess);
      this.score = this.words.size;
      UiManager.updateScore(this.score);
      UiManager.updateWordList(guess);
      UiManager.displayMessage(message, 'success');
    } else {
      UiManager.displayMessage(message, 'error');
    }

    UiManager.resetForm();
  }

  /** 
   * Decrease Timer by 1. If timer hits 0, end the game.  
   */
  countdown() {
    this.seconds = this.seconds - 1;
    UiManager.updateTimer(this.seconds)

    if (this.seconds == 0) {
      clearInterval(this.timer);
      this.scoreGame(this.score);
    }
  }

  /**
   * Log users game and check for highscore. 
   * @param {(number|string)} score the score for the game played. 
   */
  async scoreGame(score) {
    const resp = await axios.post('/score-game', { score })
    UiManager.disableForm();
    UiManager.endGameModal();
  }

  /**
   * Construct a message for the user based on the result & guess. 
   * @param {string} result  Result from the server response. 
   * @param {string} guess The guess that was submitted by the user. 
   * @returns {(string| undefined)} Returns a message for the user. 
   */
  _buildMessage(result, guess) {
    const userMessages = {
      "ok": `"${guess}" is valid, nice work!`,
      "not-word": `"${guess}" is not a valid word. Try again.`,
      "not-on-board": `"${guess}" cannot be formed on the board, Try Again.`,
    }
    return userMessages[result]
  }
}

/* Start new game on pagee load.  */
$(document).ready(() => {
  let game = new BoggleGame();
})