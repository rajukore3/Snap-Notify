const { TwitterApi } = require("twitter-api-v2");

const client = new TwitterApi({
  appKey: "bRbS4ryx9tDN4KYEEEl30xZPw",
  appSecret: "cQ8ta4rtzJV4PbSIYyqB5mFWqgnk2lKdmPiXK1a6Isu1nY5kjh",
  accessToken: "1357320175721213953-jrc37sgIDOyjjJKH0kl5eA4tveYeVA",
  accessSecret: "ng8GZHIAdf6NBQwnZMz0JcxU11HbZVTJqX8HOwQDAEee0",
  bearerToken:
    "AAAAAAAAAAAAAAAAAAAAAAsQsQEAAAAAWM7SD3VbPbwfO7unSJiYcJgxSlA%3Drt4yY3DtDNDFO9BwvGWfHqclJoMcGevQjevyS8EbYjiDTSCrjQ",
});

const rwClient = client.readWrite;

async function postTweet() {
  try {
    const mediaId = await client.v1.uploadMedia(
      "C:\\Users\\korer\\OneDrive\\Desktop\\ThemeProj\\uploaded_image.jpg"
    );

    const argumentsJson = process.argv[2];
    const arguments = JSON.parse(argumentsJson);

    // Process the arguments
    console.log('Received arguments:', arguments);
    const governmentOfficials = ['@DHANUSH34990276'];
    const tweetText = `Dear ${governmentOfficials.join(
      ',\n '
    )}, There are numerous potholes in my area that urgently need attention. Can you please take action to fix them? #PotholeIssue\n`;

    await client.readWrite.v2.tweet({
      text: tweetText + "\nLatitude: " + arguments["Latitude"] + "\nLongitude: " + arguments["Longitude"],
      media: {
        media_ids: [mediaId],
      },
    });

    console.log('Tweet posted successfully!');
  } catch (error) {
    console.error('Error posting tweet:', error);
  }
}

postTweet();
