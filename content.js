(() => {
  'use strict';
  const root=document.documentElement;
  root.classList.add('motion-opt-in');
  if(document.body.classList.contains('content-page')) {
    const menu=document.querySelector('#mobile-menu');
    const button=document.querySelector('.menu-toggle');
    const close=()=>{menu.hidden=true;button.setAttribute('aria-expanded','false');button.innerHTML='Menu <span aria-hidden="true">+</span>';};
    button.addEventListener('click',()=>{const open=menu.hidden;menu.hidden=!open;button.setAttribute('aria-expanded',String(open));button.innerHTML=open?'Close <span aria-hidden="true">−</span>':'Menu <span aria-hidden="true">+</span>';});
    menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
    addEventListener('keydown',e=>{if(e.key==='Escape'&&!menu.hidden){close();button.focus();}});
    matchMedia('(min-width:761px)').addEventListener('change',e=>{if(e.matches)close();});
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('in-view');observer.unobserve(entry.target);}}),{threshold:.05});
    document.querySelectorAll('.article-section,.page-photo').forEach(e=>observer.observe(e));
  }
  document.querySelectorAll('[data-faq-filter]').forEach(button=>button.addEventListener('click',()=>{
    const scope=button.closest('.home-faq')||button.closest('#questions');
    const choice=button.dataset.faqFilter;
    scope.querySelectorAll('[data-faq-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
    scope.querySelectorAll('[data-faq-group]').forEach(group=>{
      group.hidden=choice!=='all'&&group.dataset.faqGroup!==choice;
      if(!group.hidden)group.animate([{opacity:.4,transform:'translateY(10px)'},{opacity:1,transform:'translateY(0)'}],{duration:320,easing:'ease-out'});
    });
  }));
  document.querySelectorAll('.faq-item').forEach(item=>item.addEventListener('toggle',()=>{
    if(item.open)item.querySelector('.faq-answer').animate([{opacity:0,transform:'translateY(-8px)'},{opacity:1,transform:'translateY(0)'}],{duration:340,easing:'cubic-bezier(.2,.7,.3,1)'});
  }));
  const form=document.querySelector('#enquiry-form');
  if(form)form.addEventListener('submit',e=>{
    e.preventDefault();const data=new FormData(form);
    const message=`Hello Dhaka AD, I'm ${String(data.get('name')).trim()}.\n${data.get('brand')?'Brand: '+String(data.get('brand')).trim()+'\n':''}My campaign brief: ${String(data.get('brief')).trim()}`;
    window.open('https://wa.me/8801840860284?text='+encodeURIComponent(message),'_blank','noopener,noreferrer');
  });
})();
