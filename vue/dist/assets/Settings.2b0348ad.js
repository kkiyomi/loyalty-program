import{o as r,c as n,d as e,b as a,A as t,a as s,$ as d,a0 as o,C as i,f as l,F as c}from"./vendor.57054f9a.js";const m={name:"Account",setup(){}},g=e('<div class="mt-10 sm:mt-0"><div class="\r\n          md:grid md:grid-cols-7\r\n          md:gap-6\r\n          bg-white\r\n          dark:bg-gray-900\r\n          shadow\r\n          sm:rounded-md\r\n          px-4\r\n          py-6\r\n        "><div class="md:col-span-2 pt-2"><div class="px-4 sm:px-0"><h3 class="\r\n                text-lg\r\n                font-medium\r\n                leading-6\r\n                text-gray-900\r\n                dark:text-white\r\n              "> Account </h3><p class="mt-1 text-sm text-gray-600 dark:text-gray-300"> When changing your email, you will need to confirm your new email first. </p></div></div><div class="\r\n            md:col-span-5\r\n            mt-5\r\n            md:mt-0\r\n            overflow-hidden\r\n            sm:rounded-md\r\n            bg-white\r\n            dark:bg-gray-800\r\n          "><div class="px-4 py-5 sm:p-6"><div class="grid grid-cols-6 gap-6"><div class="col-span-6 sm:col-span-3"><label for="Username" class="\r\n                    block\r\n                    text-sm\r\n                    font-medium\r\n                    text-gray-700\r\n                    dark:text-gray-200\r\n                  "> Username </label><input type="text" name="Username" id="Username" autocomplete="Username" class="\r\n                    mt-1\r\n                    focus:ring-indigo-500\r\n                    focus:border-indigo-500\r\n                    dark:focus:bg-gray-900\r\n                    block\r\n                    w-full\r\n                    shadow-sm\r\n                    sm:text-sm\r\n                    border-gray-300\r\n                    rounded-md\r\n                    dark:bg-gray-800\r\n                    dark:text-gray-300\r\n                    dark:border-gray-600\r\n                  "></div><div class="col-span-6 sm:col-span-4"><label for="email-address" class="\r\n                    block\r\n                    text-sm\r\n                    font-medium\r\n                    text-gray-700\r\n                    dark:text-gray-200\r\n                  "> Email address </label><input type="text" name="email-address" id="email-address" autocomplete="email" class="\r\n                    mt-1\r\n                    focus:ring-indigo-500\r\n                    focus:border-indigo-500\r\n                    dark:focus:bg-gray-900\r\n                    block\r\n                    w-full\r\n                    shadow-sm\r\n                    sm:text-sm\r\n                    border-gray-300\r\n                    rounded-md\r\n                    dark:bg-gray-800\r\n                    dark:text-gray-300\r\n                    dark:border-gray-600\r\n                  "></div></div></div><div class="px-4 py-3 text-right sm:px-6"><button type="submit" class="\r\n                inline-flex\r\n                justify-center\r\n                py-2\r\n                px-4\r\n                border border-transparent\r\n                shadow-sm\r\n                text-sm\r\n                font-medium\r\n                rounded-md\r\n                text-white\r\n                bg-indigo-600\r\n                hover:bg-indigo-700\r\n                focus:outline-none\r\n                focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500\r\n              "> Save </button></div></div></div></div>',1);m.render=function(e,a,t,s,d,o){return r(),n("div",null,[g])};const u={name:"Profile",setup(){}},p=a("div",null,[a("div",{class:"md:grid md:grid-cols-7 md:gap-6"},[a("div",{class:"md:col-span-2"},[a("div",{class:"px-4 sm:px-0"},[a("h3",{class:"\r\n                text-lg\r\n                font-medium\r\n                leading-6\r\n                text-gray-900\r\n                dark:text-white\r\n              "}," Profile "),a("p",{class:"mt-1 text-sm text-gray-600 dark:text-gray-300"}," This information will be displayed publicly so be careful what you share. ")])]),a("div",{class:"mt-5 md:mt-0 md:col-span-5"},[a("div",null,[a("div",{class:"shadow sm:rounded-md sm:overflow-hidden"},[a("div",{class:"px-4 py-5 bg-white dark:bg-gray-800 space-y-6 sm:p-6"},[a("div",{class:"grid grid-cols-3 gap-6"},[a("div",{class:"col-span-3 sm:col-span-2"},[a("label",{for:"company-website",class:"\r\n                        block\r\n                        text-sm\r\n                        font-medium\r\n                        text-gray-700\r\n                        dark:text-gray-200\r\n                      "}," Website "),a("div",{class:"mt-1 flex rounded-md shadow-sm"},[a("span",{class:"\r\n                          inline-flex\r\n                          items-center\r\n                          px-3\r\n                          rounded-l-md\r\n                          border border-r-0 border-gray-300\r\n                          bg-gray-50\r\n                          text-gray-500 text-sm\r\n                          dark:bg-gray-800\r\n                          dark:text-gray-300\r\n                          dark:border-gray-600\r\n                        "}," http:// "),a("input",{type:"text",name:"company-website",id:"company-website",class:"\r\n                          focus:ring-indigo-500\r\n                          focus:border-indigo-500\r\n                          flex-1\r\n                          block\r\n                          w-full\r\n                          rounded-none rounded-r-md\r\n                          sm:text-sm\r\n                          border-gray-300\r\n                          dark:bg-gray-800\r\n                          dark:text-gray-300\r\n                          dark:border-gray-600\r\n                          dark:placeholder-gray-300\r\n                        ",placeholder:"www.example.com"})])])]),a("div",null,[a("label",{for:"about",class:"\r\n                      block\r\n                      text-sm\r\n                      font-medium\r\n                      text-gray-700\r\n                      dark:text-gray-200\r\n                    "}," About "),a("div",{class:"mt-1"},[a("textarea",{id:"about",name:"about",rows:"3",class:"\r\n                        shadow-sm\r\n                        focus:ring-indigo-500\r\n                        focus:border-indigo-500\r\n                        mt-1\r\n                        block\r\n                        w-full\r\n                        sm:text-sm\r\n                        border border-gray-300\r\n                        rounded-md\r\n                        dark:bg-gray-800\r\n                        dark:text-gray-300\r\n                        dark:border-gray-600\r\n                        dark:placeholder-gray-300\r\n                      ",placeholder:"you@example.com"})]),a("p",{class:"mt-2 text-sm text-gray-500 dark:text-gray-200"}," Brief description for your profile. URLs are hyperlinked. ")]),a("div",null,[a("label",{class:"\r\n                      block\r\n                      text-sm\r\n                      font-medium\r\n                      text-gray-700\r\n                      dark:text-gray-200\r\n                    "}," Photo "),a("div",{class:"mt-1 flex items-center"},[a("span",{class:"\r\n                        inline-block\r\n                        h-12\r\n                        w-12\r\n                        rounded-full\r\n                        overflow-hidden\r\n                        bg-gray-100\r\n                      "},[a("svg",{class:"h-full w-full text-gray-300",fill:"currentColor",viewBox:"0 0 24 24"},[a("path",{d:"M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z"})])]),a("button",{type:"button",class:"\r\n                        ml-5\r\n                        bg-white\r\n                        py-2\r\n                        px-3\r\n                        border border-gray-300\r\n                        rounded-md\r\n                        shadow-sm\r\n                        text-sm\r\n                        leading-4\r\n                        font-medium\r\n                        text-gray-700\r\n                        hover:bg-gray-50\r\n                        focus:outline-none\r\n                        focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500\r\n                      "}," Change ")])]),a("div",null,[a("label",{class:"\r\n                      block\r\n                      text-sm\r\n                      font-medium\r\n                      text-gray-700\r\n                      dark:text-gray-300\r\n                    "}," Cover photo "),a("div",{class:"\r\n                      mt-1\r\n                      flex\r\n                      justify-center\r\n                      px-6\r\n                      pt-5\r\n                      pb-6\r\n                      border-2 border-gray-300 border-dashed\r\n                      rounded-md\r\n                    "},[a("div",{class:"space-y-1 text-center"},[a("svg",{class:"mx-auto h-12 w-12 text-gray-400",stroke:"currentColor",fill:"none",viewBox:"0 0 48 48","aria-hidden":"true"},[a("path",{d:"M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round"})]),a("div",{class:"flex text-sm text-gray-600"},[a("label",{for:"file-upload",class:"\r\n                            relative\r\n                            cursor-pointer\r\n                            bg-white\r\n                            rounded-md\r\n                            font-medium\r\n                            text-indigo-600\r\n                            hover:text-indigo-500\r\n                            focus-within:outline-none\r\n                            focus-within:ring-2\r\n                            focus-within:ring-offset-2\r\n                            focus-within:ring-indigo-500\r\n                          "},[a("span",null,"Upload a file"),a("input",{id:"file-upload",name:"file-upload",type:"file",class:"sr-only"})]),a("p",{class:"pl-1"},"or drag and drop")]),a("p",{class:"text-xs text-gray-500"}," PNG, JPG, GIF up to 10MB ")])])])]),a("div",{class:"\r\n                  px-4\r\n                  py-3\r\n                  text-right\r\n                  bg-gray-50\r\n                  dark:bg-gray-800\r\n                  dark:border-t dark:border-gray-700\r\n                  sm:px-6\r\n                "},[a("button",{type:"submit",class:"\r\n                    inline-flex\r\n                    justify-center\r\n                    py-2\r\n                    px-4\r\n                    border border-transparent\r\n                    shadow-sm\r\n                    text-sm\r\n                    font-medium\r\n                    rounded-md\r\n                    text-white\r\n                    bg-indigo-600\r\n                    hover:bg-indigo-700\r\n                    focus:outline-none\r\n                    focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500\r\n                  "}," Save ")])])])])])],-1);u.render=function(e,a,t,s,d,o){return r(),n("div",null,[p])};const b={name:"SettingsView",components:{Account:m,Profile:u},setup:()=>({activeTab:t("account"),tabs:s([{title:"Account",tabName:"account"},{title:"Profile",tabName:"profile"}])})},f={class:"grid grid-cols-5 w-full h-full sm:p-4 gap-6 lg:px-16"},x={class:"col-span-5 md:col-span-1 leading-6 dark:text-white"},y={class:"col-span-5 md:col-span-4"};b.render=function(e,t,s,m,g,u){const p=l("Account"),b=l("Profile");return r(),n("div",f,[a("div",x,[(r(!0),n(d,null,o(m.tabs,(e=>(r(),n("button",{key:e.index,class:["block p-2 my-2 rounded-md w-full text-sm text-left",m.activeTab===e.tabName?"bg-gray-300 dark:text-gray-900":"hover:bg-gray-300 dark:hover:bg-gray-500 "],onClick:r=>m.activeTab=e.tabName},c(e.title),11,["onClick"])))),128))]),a("div",y,["account"===m.activeTab?(r(),n(p,{key:0})):i("",!0),"profile"===m.activeTab?(r(),n(b,{key:1})):i("",!0)])])};export default b;
