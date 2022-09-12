#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;
axios.get(url)
  .then(function (response) {
    const userTask = {};
    let taskCount = 0;
    let task;
    let userId = response.data[0].userId;
    for (task of response.data) {
      if (task.userId !== userId) {
        if (taskCount > 0) {
          userTask[userId] = taskCount;
        }
        userId = task.userId;
        taskCount = 0;
      }
      if (task.completed === true) {
        taskCount += 1;
      }
    }
    if (taskCount > 0) {
      userTask[userId] = taskCount;
    }
    console.log(userTask);
  });
