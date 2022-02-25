<template>
  <div class="fixed top-60 left-[16.666667%] sm:left-1/4
    bg-tblack-500 text-white
    border-2
    border-white
    rounded-md
    justify-self-center
    ease-in-out
    opacity-0 h-0 -mt-20
    transition-all
    w-2/3 md:w-1/2
    outline-none 
    overflow-x-hidden overflow-y-auto"
  id="logoutModal" tabindex="-1">
    <div class="border-none shadow-lg relative flex flex-col w-full pointer-events-auto rounded-md outline-none">
    <h5 class="text-xl font-medium p-4" id="logoutModalLabel">Déconnexion</h5>
    <div class="relative p-4">
      Voulez vous vraiment vous déconnecter ?
    </div>
    <div class="flex-col-reverse sm:flex-row flex items-center justify-end p-4 rounded-b-md">
      <button type="button" class="btn-secondary" onclick="closeModal('logoutModal')">Annuler</button>
      <a href=""><button class="btn-primary ml-1 mb-3 sm:mb-0">Déconnexion</button></a>
    </div>
    </div>
  </div>
</template>