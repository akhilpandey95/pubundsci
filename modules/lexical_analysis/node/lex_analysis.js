/* This Source Code Form is subject to the terms of the MPL
 * License. If a copy of the same was not distributed with this
 * file, You can obtain one at
 https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.*/

const nlp = require("natural");
const colors = require("colors");

module.exports.predict = (foo, bar) => {
    nlp.PorterStemmer.attach();
    process.stdout.write(`${"A".bold.underline.white}: ${foo.tokenizeAndStem().toString().bold.yellow}\n`);
    process.stdout.write(`${"B".bold.underline.white}: ${bar.tokenizeAndStem().toString().bold.yellow}\n`);
    process.stdout.write(`${"Similarity Score:".bold.red} ${"somescore".bold.green}\n`);
}
