<html>
<script>
    function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function start_me() {
    await sleep(2000);
        location.href = '/';
}

start_me();

</script>
<body>
Nope!
</body>

</html>