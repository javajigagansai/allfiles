<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit;
}

include 'db.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | User Auth</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main class="auth-shell">
        <div class="card">
            <div class="shell-head">
                <p class="eyebrow">Dashboard</p>
                <h1>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?>!</h1>
                <p class="hint">You are signed in and can now access protected content.</p>
            </div>

            <div class="stack top-space">
                <p class="muted">This is a placeholder dashboard. Add your app content here.</p>
                <a class="btn secondary" href="logout.php">Log out</a>
            </div>
        </div>
    </main>
</body>
</html>
