<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SleepInvader</title>

  <!-- =====================================================
    SleepInvader - HSC Software Engineering Task #2
    Student: Ignatius H.
    Date: March 2026

    BAND 3 STARTING POINT
    This prototype is partially complete. It demonstrates
    basic Create and Read functionality. Update and Delete
    are not yet implemented.

    Passwords are stored as plain text - this is NOT secure.
    See the TODO comments to find out how to fix this.
    ===================================================== -->

  <style>
    /* Dark Mode Base */
    body {
      font-family: "Inter", "Source Sans Pro", Arial, sans-serif;
      background-color: #0f1115;
      color: #e5e7eb;
      margin: 0;
      padding: 0;
    }
    /* Top Bar */
    .topbar {
      background-color: #111827;
      color: #f3f4f6;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .topbar h1 {
      margin: 0;
      font-size: 20px;
    }

    /* Main Layout */
    .container {
      max-width: 900px;
      margin: 30px auto;
      padding: 0 20px;
    }

    /* Cards */
    .card {
      background: #1f2937;
      border: 1px solid #374151;
      border-radius: 6px;
      padding: 24px;
      margin-bottom: 20px;
    }

    .card h2 {
      margin-top: 0;
      color: #93c5fd;
      font-size: 18px;
      border-bottom: 1px solid #374151;
      padding-bottom: 10px;
    }

    /* Form Styles */
    label {
      display: block;
      font-size: 14px;
      font-weight: bold;
      margin-bottom: 4px;
      margin-top: 12px;
      color: #e5e7eb;
    }

    input, select, textarea {
      width: 100%;
      padding: 8px 10px;
      border: 1px solid #4b5563;
      border-radius: 4px;
      font-size: 14px;
      background-color: #111827;
      color: #f3f4f6;
      box-sizing: border-box;
    }

    /* Focus State */
    input:focus, select:focus, textarea:focus {
      border-color: #3b82f6;
      outline: none;
      box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.4);
    }

    /* Buttons */
    .btn {
      padding: 9px 18px;
      border: none;
      border-radius: 4px;
      font-size: 14px;
      cursor: pointer;
      margin-top: 14px;
    }

    /* Primary Button */
    .btn-primary {
      background-color: #2563eb;
      color: white;
    }

    .btn-primary:hover {
      background-color: #1d4ed8;
    }

    /* Danger Button */
    .btn-danger {
      background-color: #dc2626;
      color: white;
    }

    .btn-danger:hover {
      background-color: #b91c1c;
    }

    /* Messages */
    .error-msg {
      color: #f87171;
      font-size: 13px;
      margin-top: 6px;
    }

    .success-msg {
      color: #4ade80;
      font-size: 13px;
      margin-top: 6px;
    }

    /* Table */
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
      color: #e5e7eb;
    }

    th {
      background-color: #111827;
      color: #f3f4f6;
      padding: 10px 12px;
      text-align: left;
    }

    td {
      padding: 10px 12px;
      border-bottom: 1px solid #374151;
    }

    tr:hover {
      background-color: #1f2937;
    }

    /* Auth Forms */
    .auth-wrap {
      max-width: 400px;
      margin: 60px auto;
      padding: 0 20px;
    }

    .auth-wrap h1 {
      color: #93c5fd;
      text-align: center;
      margin-bottom: 6px;
    }

    .auth-wrap p {
      text-align: center;
      color: #9ca3af;
      font-size: 14px;
      margin-bottom: 24px;
    }

    /* Page Visibility */
    .page { display: none; }
    .page.active { display: block; }

    /* Stats Row */
    .stats-row {
      display: flex;
      gap: 16px;
      margin-bottom: 20px;
    }

    .stat-box {
      background: #1f2937;
      border: 1px solid #374151;
      border-radius: 6px;
      padding: 16px 20px;
      flex: 1;
      text-align: center;
    }

    .stat-box .stat-num {
      font-size: 28px;
      font-weight: bold;
      color: #93c5fd;
    }

    .stat-box .stat-label {
      font-size: 12px;
      color: #9ca3af;
      margin-top: 4px;
    }
  </style>
</head>
<body>

<!-- =====================================================
  PAGE: LOGIN
  This is shown when the user is not logged in.
===================================================== -->
<div class="page active" id="page-login">
  <div class="auth-wrap">
    <h1>😴 SleepInvader</h1>
    <p>Log in to track your sleep sessions.</p>

    <div class="card">
      <h2>Login</h2>

      <label for="loginEmail">Email</label>
      <input type="email" id="loginEmail" placeholder="your@email.com">

      <label for="loginPassword">Password</label>
      <input type="password" id="loginPassword" placeholder="Password">

      <!-- Error message area - hidden until needed -->
      <div class="error-msg" id="loginError" style="display:none"></div>

      <button class="btn btn-primary" onclick="doLogin()">Sign In</button>

      <p style="font-size:13px; margin-top:14px; color:#666;">
        No account? <a href="#" onclick="showPage('page-register')">Register here</a>
      </p>
    </div>

    <!-- Dev helper - remove before final submission -->
    <div style="background:#fffde7; border:1px solid #f59e0b; border-radius:4px; padding:10px; font-size:12px; color:#92400e; margin-top:12px;">
      <strong>Test login:</strong> demo@test.com / password123
    </div>
  </div>
</div>


<!-- =====================================================
  PAGE: REGISTER
  New users create an account here.
===================================================== -->
<div class="page" id="page-register">
  <div class="auth-wrap">
    <h1>😴 SleepInvader</h1>
    <p>Create your account to get started.</p>

    <div class="card">
      <h2>Register</h2>

      <label for="regName">Full Name</label>
      <input type="text" id="regName" placeholder="Jane Smith">

      <label for="regEmail">Email</label>
      <input type="email" id="regEmail" placeholder="your@email.com">

      <label for="regPassword">Password</label>
      <input type="password" id="regPassword" placeholder="Choose a password">

      <!-- TODO (Band 4): Add a "Confirm Password" field and
           check both passwords match before registering.
           <label for="regConfirm">Confirm Password</label>
           <input type="password" id="regConfirm"> -->

      <div class="error-msg" id="registerError" style="display:none"></div>

      <button class="btn btn-primary" onclick="doRegister()">Create Account</button>

      <p style="font-size:13px; margin-top:14px; color:#666;">
        Already have an account? <a href="#" onclick="showPage('page-login')">Login here</a>
      </p>
    </div>
  </div>
</div>


<!-- =====================================================
  PAGE: DASHBOARD
  Main app view - shown after login.
===================================================== -->
<div class="page" id="page-dashboard">

  <!-- Top bar -->
  <div class="topbar">
    <h1>😴 SleepInvader</h1>
    <div>
      <span id="welcomeMsg" style="font-size:14px; margin-right:16px;"></span>
      <button class="btn btn-primary" style="margin-top:0; padding:6px 14px; font-size:13px;" onclick="doLogout()">Logout</button>
    </div>
  </div>

  <div class="container">

    <!-- Stats row -->
    <div class="stats-row">
      <div class="stat-box">
        <div class="stat-num" id="statTotal">0</div>
        <div class="stat-label">Total Sessions</div>
      </div>
      <div class="stat-box">
        <div class="stat-num" id="statHours">0</div>
        <div class="stat-label">Average Hours / Night</div>
      </div>
      <div class="stat-box">
        <div class="stat-num" id="statSubjects">0</div>
        <div class="stat-label">Different Bedtimes</div>
      </div>
      <!-- TODO (Band 4): Add a "This Week" stat box that only
           counts sessions from the last 7 days. You will need
           to compare session dates to today's date using
           the JavaScript Date object. -->
    </div>

    <!-- Add Session Form -->
    <div class="card">
      <h2>Log a Sleep Session</h2>

      <label for="sessionDate">Date</label>
      <input type="date" id="sessionDate">

      <label for="sessionSubject">Bedtime</label>
      <!-- TODO (Band 4-5): Replace this plain text input with a
           <select> dropdown that is populated from the subjects
           the user has added. This requires a separate subjects
           list stored in localStorage and a function to build
           the dropdown options dynamically. -->
      <input type="text" id="sessionSubject" placeholder="e.g. 7:00pm">

      <label for="sessionMins">Duration (hours)</label>
      <input type="number" id="sessionMins" placeholder="e.g. 9.5" min="1">

      <label for="sessionNotes">Notes (optional)</label>
      <textarea id="sessionNotes" rows="3" placeholder="How well did you sleep?"></textarea>

      <div class="error-msg" id="sessionError" style="display:none"></div>

      <button class="btn btn-primary" onclick="addSession()">Save Session</button>
    </div>

    <!-- Sessions List -->
    <div class="card">
      <h2>My Sessions</h2>

      <!-- TODO (Band 4): Add a search input here that filters
           the table as the user types. You will need to loop
           through the sessions and check if the subject name
           contains the search text. -->

      <div id="sessionsContainer">
        <!-- Sessions table is built here by JavaScript -->
        <p style="color:#888; font-size:14px;">No sessions yet. Add one above.</p>
      </div>
    </div>

    <!-- TODO (Band 4-5): Add a Subjects management section
         here so users can add and manage their subject list.
         This is needed to populate the subject dropdown above.
         Structure:
         <div class="card">
           <h2>My Subjects</h2>
           ... add subject form ...
           ... subjects list ...
         </div>  -->

  </div><!-- end .container -->
</div><!-- end #page-dashboard -->


<!-- =====================================================
  JAVASCRIPT
  All the app logic is below.
===================================================== -->
<script>

  // ===================================================
  // DATA STORAGE
  // We use localStorage to save data in the browser.
  // This means data stays saved when you close the tab.
  //
  // TODO (Band 5): In a real web app you would replace
  // localStorage with a server-side database like SQLite
  // or PostgreSQL. The equivalent SQL query for loading
  // sessions would be:
  //   SELECT * FROM sessions WHERE user_id = ?
  // ===================================================

  // Load users array from storage, or start with empty array
  // We pre-load a demo user so students can test immediately
  function getUsers() {
    var stored = localStorage.getItem('st_users');
    if (stored) {
      return JSON.parse(stored);
    }
    // Default demo user
    // TODO (Band 4): Remove this hardcoded demo user once
    // the register form is working properly.
    return [
      {
        id: 1,
        name: 'Demo User',
        email: 'demo@test.com',
        // TODO (CRITICAL - Band 4/5): This password is stored
        // in plain text. This is a major security issue.
        // In a real app you must HASH passwords before storing.
        // With Flask + bcrypt:
        //   hashed = bcrypt.generate_password_hash(password)
        // To check: bcrypt.check_password_hash(hashed, input)
        password: 'password123'
      }
    ];
  }

  function saveUsers(users) {
    localStorage.setItem('st_users', JSON.stringify(users));
  }

  // Load sessions for the current user
  function getSessions() {
    var stored = localStorage.getItem('st_sessions');
    if (!stored) return [];
    var all = JSON.parse(stored);
    // Only return sessions belonging to the logged-in user
    return all.filter(function(s) {
      return s.userId == currentUserId;
    });
  }

  function saveSessions(sessions) {
    // Load all sessions (all users), replace this user's sessions
    var stored = localStorage.getItem('st_sessions');
    var all = stored ? JSON.parse(stored) : [];
    // Remove old sessions for this user
    var others = all.filter(function(s) {
      return s.userId != currentUserId;
    });
    // Add the updated sessions back
    var combined = others.concat(sessions);
    localStorage.setItem('st_sessions', JSON.stringify(combined));
  }

  // Track who is logged in
  // This is just stored as a number (user ID)
  var currentUserId = null;

  // ===================================================
  // HELPER: simple ID generator
  // Each new record needs a unique ID
  // TODO (Band 5): In a real database, the ID would be
  // auto-generated by the database (e.g. INTEGER PRIMARY KEY
  // AUTOINCREMENT in SQLite). Here we just use Date.now()
  // which gives us a number based on the current time.
  // ===================================================
  function makeId() {
    return Date.now();
  }

  // ===================================================
  // PAGE NAVIGATION
  // Shows one page and hides all others
  // ===================================================
  function showPage(pageId) {
    var pages = document.querySelectorAll('.page');
    for (var i = 0; i < pages.length; i++) {
      pages[i].classList.remove('active');
    }
    document.getElementById(pageId).classList.add('active');
  }

  // ===================================================
  // AUTH: LOGIN
  // Checks the entered email and password against stored users
  // ===================================================
  function doLogin() {
    var email    = document.getElementById('loginEmail').value;
    var password = document.getElementById('loginPassword').value;
    var errorEl  = document.getElementById('loginError');

    // Basic check - fields not empty
    if (email == '' || password == '') {
      errorEl.textContent = 'Please fill in all fields.';
      errorEl.style.display = 'block';
      return;
    }

    // TODO (Band 4): Add email format validation here.
    // A simple check is to see if the email contains '@' and '.'
    // e.g. if (!email.includes('@')) { ... show error ... }

    // Look for a matching user
    var users = getUsers();
    var found = null;
    for (var i = 0; i < users.length; i++) {
      if (users[i].email == email && users[i].password == password) {
        found = users[i];
        break;
      }
    }

    if (found == null) {
      errorEl.textContent = 'Incorrect email or password.';
      errorEl.style.display = 'block';
      return;
    }

    // Login successful
    errorEl.style.display = 'none';
    currentUserId = found.id;

    // Save to localStorage so user stays logged in on refresh
    localStorage.setItem('st_currentUser', found.id);

    // Go to dashboard
    showPage('page-dashboard');
    document.getElementById('welcomeMsg').textContent = 'Hello, ' + found.name;
    refreshDashboard();
  }

  // ===================================================
  // AUTH: REGISTER
  // Creates a new user account
  // ===================================================
  function doRegister() {
    var name     = document.getElementById('regName').value;
    var email    = document.getElementById('regEmail').value;
    var password = document.getElementById('regPassword').value;
    var errorEl  = document.getElementById('registerError');

    // Check fields are not empty
    if (name == '' || email == '' || password == '') {
      errorEl.textContent = 'Please fill in all fields.';
      errorEl.style.display = 'block';
      return;
    }

    // Check email not already taken
    var users = getUsers();
    for (var i = 0; i < users.length; i++) {
      if (users[i].email == email) {
        errorEl.textContent = 'An account with that email already exists.';
        errorEl.style.display = 'block';
        return;
      }
    }

    // TODO (Band 4): Add password length check here.
    // Minimum 8 characters is a common requirement.
    // if (password.length < 8) { ... show error ... }

    // TODO (CRITICAL - Band 4/5): Hash the password before
    // saving it. In this prototype we save it as plain text
    // which means anyone who reads localStorage can see it.
    // In a real Flask app:
    //   password_hash = bcrypt.generate_password_hash(password)
    //   store password_hash, NOT password

    // Create the new user object
    var newUser = {
      id:       makeId(),
      name:     name,
      email:    email,
      password: password   // <-- plain text: fix this!
    };

    users.push(newUser);
    saveUsers(users);

    // Auto-login the new user
    currentUserId = newUser.id;
    localStorage.setItem('st_currentUser', newUser.id);

    showPage('page-dashboard');
    document.getElementById('welcomeMsg').textContent = 'Hello, ' + newUser.name;
    refreshDashboard();
  }

  // ===================================================
  // AUTH: LOGOUT
  // ===================================================
  function doLogout() {
    currentUserId = null;
    localStorage.removeItem('st_currentUser');
    showPage('page-login');
  }

  // ===================================================
  // CREATE: Add a new session
  // SQL equivalent:
  //   INSERT INTO sessions (user_id, date, subject,
  //     duration_mins, notes) VALUES (?, ?, ?, ?, ?)
  // ===================================================
  function addSession() {
    var date     = document.getElementById('sessionDate').value;
    var subject  = document.getElementById('sessionSubject').value.trim();
    var mins     = document.getElementById('sessionMins').value;
    var notes    = document.getElementById('sessionNotes').value.trim();
    var errorEl  = document.getElementById('sessionError');

    // Validate required fields
    if (date == '' || subject == '' || mins == '') {
      errorEl.textContent = 'Date, subject, and duration are required.';
      errorEl.style.display = 'block';
      return;
    }

    if (parseInt(mins) <= 0) {
      errorEl.textContent = 'Duration must be greater than zero.';
      errorEl.style.display = 'block';
      return;
    }

    // TODO (Band 4): Add more validation:
    // - Check the date is not in the future
    // - Check subject name isn't too long (e.g. max 50 chars)
    // - Check minutes isn't unrealistically large (e.g. max 480)

    // Clear error
    errorEl.style.display = 'none';

    // Build the session object
    var session = {
      id:          makeId(),
      userId:      currentUserId,
      date:        date,
      subject:     subject,
      durationMins: parseInt(mins),
      notes:       notes
    };

    // Add to the sessions array and save
    var sessions = getSessions();
    sessions.push(session);
    saveSessions(sessions);

    // Clear the form
    document.getElementById('sessionDate').value    = '';
    document.getElementById('sessionSubject').value = '';
    document.getElementById('sessionMins').value    = '';
    document.getElementById('sessionNotes').value   = '';

    // Refresh the sessions table
    refreshDashboard();
  }

  // ===================================================
  // READ: Load and display all sessions in a table
  // SQL equivalent:
  //   SELECT * FROM sessions WHERE user_id = ?
  //   ORDER BY date DESC
  // ===================================================
  function refreshDashboard() {
    var sessions = getSessions();
    var container = document.getElementById('sessionsContainer');

    // Update stats
    document.getElementById('statTotal').textContent = sessions.length;

    var totalMins = 0;
    var subjectSet = {};
    for (var i = 0; i < sessions.length; i++) {
      totalMins += sessions[i].durationMins;
      subjectSet[sessions[i].subject] = true;
    }
    document.getElementById('statHours').textContent = (totalMins / 60).toFixed(1) + 'h';
    document.getElementById('statSubjects').textContent = Object.keys(subjectSet).length;

    // Show empty message if no sessions
    if (sessions.length == 0) {
      container.innerHTML = '<p style="color:#888; font-size:14px;">No sessions yet. Add one above.</p>';
      return;
    }

    // Sort by date, newest first
    sessions.sort(function(a, b) {
      return new Date(b.date) - new Date(a.date);
    });

    // Build the HTML table
    var html = '<table>';
    html += '<thead><tr>';
    html += '<th>Date</th>';
    html += '<th>Subject</th>';
    html += '<th>Duration</th>';
    html += '<th>Notes</th>';
    // TODO (Band 4): Add an Actions column header here for
    // Edit and Delete buttons:
    // html += '<th>Actions</th>';
    html += '</tr></thead>';
    html += '<tbody>';

    for (var i = 0; i < sessions.length; i++) {
      var s = sessions[i];
      html += '<tr>';
      html += '<td>' + s.date + '</td>';
      html += '<td>' + s.subject + '</td>';
      html += '<td>' + s.durationMins + ' hrs</td>';
      html += '<td>' + (s.notes || '—') + '</td>';

      // TODO (Band 4 - DELETE): Add a delete button here.
      // You need to pass the session's id to a deleteSession()
      // function. The function should find the session by id,
      // remove it from the array, and call saveSessions() and
      // refreshDashboard() again.
      // html += '<td>';
      // html += '<button onclick="deleteSession(' + s.id + ')">Delete</button>';
      // html += '</td>';

      // TODO (Band 4-5 - UPDATE/EDIT): Add an edit button that
      // fills the form above with this session's data so the
      // user can change it and save again. This is the UPDATE
      // part of CRUD and is required for Band 4+.
      // html += '<button onclick="editSession(' + s.id + ')">Edit</button>';

      html += '</tr>';
    }

    html += '</tbody></table>';
    container.innerHTML = html;
  }

  // ===================================================
  // DELETE SESSION (not yet implemented)
  // TODO (Band 4): Build this function.
  //
  // SQL equivalent:
  //   DELETE FROM sessions WHERE id = ? AND user_id = ?
  //   (always include user_id check for security!)
  //
  // Steps:
  // 1. Get the sessions array with getSessions()
  // 2. Use .filter() to remove the session with matching id
  // 3. Call saveSessions() with the new array
  // 4. Call refreshDashboard() to update the table
  //
  // function deleteSession(id) {
  //   var sessions = getSessions();
  //   var updated = sessions.filter(function(s) {
  //     return s.id != id;
  //   });
  //   saveSessions(updated);
  //   refreshDashboard();
  // }
  // ===================================================


  // ===================================================
  // EDIT SESSION (not yet implemented)
  // TODO (Band 4-5): Build this function.
  //
  // SQL equivalent:
  //   UPDATE sessions SET date=?, subject=?, duration_mins=?,
  //   notes=? WHERE id=? AND user_id=?
  //
  // Steps:
  // 1. Find the session by id in getSessions()
  // 2. Fill the form fields with the session's data
  // 3. Store the id somewhere (e.g. a hidden input or variable)
  // 4. When the form is saved, check if we are editing (id set)
  //    and UPDATE rather than INSERT a new record
  // ===================================================


  // ===================================================
  // APP STARTUP
  // Check if someone is already logged in when the page loads
  // ===================================================
  var savedUserId = localStorage.getItem('st_currentUser');
  if (savedUserId) {
    // Someone was logged in - restore their session
    var users = getUsers();
    for (var i = 0; i < users.length; i++) {
      if (users[i].id == savedUserId) {
        currentUserId = users[i].id;
        showPage('page-dashboard');
        document.getElementById('welcomeMsg').textContent = 'Hello, ' + users[i].name;
        refreshDashboard();
        break;
      }
    }
  }
  // If no saved user, the login page is already showing (default)

  // Set today's date as default in the date field
  var today = new Date().toISOString().split('T')[0];
  document.getElementById('sessionDate').value = today;

</script>
</body>
</html>
