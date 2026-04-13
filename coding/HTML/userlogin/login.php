<?php
include 'db.php';

session_start();

$error = '';
$username = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if ($username === '' || $password === '') {
        $error = 'Please enter both username and password.';
    } else {
        $stmt = $pdo->prepare("SELECT id, username, password FROM users WHERE username = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch();

        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            header('Location: dashboard.php');
            exit;
        } else {
            $error = 'Invalid username or password.';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in | User Auth</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main class="auth-shell">
        <div class="card">
            <div class="shell-head">
                <p class="eyebrow">Account access</p>
                <h1>Sign in</h1>
                <p class="hint">Welcome back. Enter your credentials to continue.</p>
            </div>

            <?php if ($error): ?>
                <div class="alert error"><?php echo htmlspecialchars($error); ?></div>
            <?php endif; ?>

            <?php if (isset($_GET['registered'])): ?>
                <div class="alert success">Registration successful. You can sign in now.</div>
            <?php endif; ?>

            <form class="stack" action="login.php" method="post" novalidate>
                <div class="field">
                    <label for="username">Username</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        value="<?php echo htmlspecialchars($username); ?>"
                        autocomplete="username"
                        required
                    >
                </div>
                <div class="field">
                    <label for="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        autocomplete="current-password"
                        required
                    >
                </div>
                <button type="submit" class="btn">Sign in</button>
            </form>

            <div class="link-row">
                <span>Need an account?</span>
                <a href="register.php">Create one</a>
            </div>
        </div>
    </main>
</body>
</html>
