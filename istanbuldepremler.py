<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Son Depremler - EMSC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f7f7f7;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #fff;
            margin: 10px 0;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .date {
            display: block;
            margin-top: 5px;
            color: #777;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>Son Depremler (EMSC)</h1>
    <ul id="depremListesi">
        <!-- Deprem verileri buraya gelecek -->
    </ul>

    <script>
        async function veriCek() {
            const response = await fetch('depremler.json');
            const data = await response.json();

            const liste = document.getElementById('depremListesi');
            data.forEach(deprem => {
                const li = document.createElement('li');
                li.innerHTML = `<a href="${deprem.link}" target="_blank">${deprem.baslik}</a><span class="date">${deprem.tarih}</span>`;
                liste.appendChild(li);
            });
        }

        veriCek();
    </script>
</body>
</html>

