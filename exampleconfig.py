from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25058528
    API_HASH = "303cdbe35f694606532299639821683e"
    # the name to display in your alive message
    ALIVE_NAME = "SoN GoKu"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://gokublack1751:<Uo4cvrx1WeCq7cKz>@gokuuser.2d2ntgu.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMgBu4Icu9_kEwMK8KfyzPpF5QOJmPfwIN3tgVsLRlPhwG5m_ezI5SSV9fexK_7JkT2cIilVa_mKHssaDNMpxJlV1_bPHFHsxXeM1U-7tO4ite-iRGJ6ejsFoOsmxgWuv-l5a5kBEQV2X2YsSEMAwvfrYMPuS2_RMMGaSIxt9JdOFS6lATbo4VozutrZigY-IIQgGW86973cO_xftlokxE8TOQOAUtAK9LS6gvm4YgigXUaQd03nbyh4ftE7xndS-bMb8aieKXA3R126yMJalyFRBDmXjfSA2ev8zzaZA0AFSWM3jGbypLALCshYH5dbcjlnlgSLGVwv_YAefKDy3daQ3MU="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6539972715:AAHMIyQ9oHQ0Z0Yl48_PpzvguyBWj4PhQRY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -4044239653
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
