const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/story.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.screenshot({path:__dirname+'/magadhina-story.png'});
await p.addStyleTag({content:'body{background:transparent!important}'});
await p.screenshot({path:__dirname+'/magadhina-story-overlay.png',omitBackground:true});await b.close();})();
