return (
    <Container maxWidth="xs">
        <Box
            sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                mt: 8,
                p: 4,
                boxShadow: 3,
                borderRadius: 2,
                bgcolor: "background.paper"
            }}
        >
            <Typography variant="h5" component="h1" gutterBottom>
                Login
            </Typography>
            <form onSubmit={handleSubmit} style={{ width: "100%" }}>
                <TextField
                    label="Username"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <TextField
                    label="Password"
                    type="password"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <Button type="submit" variant="contained" fullWidth sx={{ mt: 2 }}>
                    Login
                </Button>
            </form>
            <Typography variant="body1" sx={{ mt: 2 }}>or</Typography>
            
            {/* Google OAuth Login */}
            <GoogleLogin onSuccess={handleGoogleLogin} onError={() => setMessage({ type: "error", text: "OAuth login failed" })} />

            {message && (
                <Alert severity={message.type} sx={{ mt: 2, width: "100%" }}>
                    {message.text}
                </Alert>
            )}
        </Box>
    </Container>
);