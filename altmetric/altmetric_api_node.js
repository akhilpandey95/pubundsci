/* Altmetric API testing
 * Akhil Pandey
 * The mIT License
 */

const https = require("https");

// https://api.altmetric.com/v1/doi/10.1038/480426a

var options = {
    host: "api.altmetric.com",
    path: "/v1/doi/10.1038/480426a",
    headers: {"User-Agent": "request"}
};

https.get(options, (res) => {
    let body = "";

    res.on("data", (chunk) => {
        body += chunk;
    });

    res.on("end", () => {
        if(res.statusCode === 200) {
            try {
                let output = JSON.parse(body);
                //process.stdout.write(`${output}\n`);
                console.log(output.title);
                console.log(res.headers);
            } catch (e) {
                process.stdout.write(`Caught an exception ${e}\n`);
            }
        } else {
            process.stdout.write(`${res.statusCode}\n`);
        }
    });
}).on("error", (err) => {
    process.stdout.write(`Caught an error ${err}\n`);
})

module.exports.fetchData = (foo, bar) => {
    return new Promise((resolve, reject) => {
        let options = {
            host : config.altmetric_api_url,
            path : config.altmetric.api_path,
            headers: {"User-Agent": "request"}
        };

        let request = https.get(options, (res) => {
            if (res.statusCode === 200) {
                let body = "";

                res.on("body", (chunk) => {
                    body += chunk;
                });

                res.on("end", () => {
                    resolve(JSON.parse(body));
                });
            } else {
                reject(new Error(res.statusCode + ": " + res.statusMessage));
            }
        });

        request.on("error", (err) => {
            reject(err);
        });
    });
}
