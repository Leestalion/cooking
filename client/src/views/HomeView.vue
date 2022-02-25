<script setup>
import LogoutDialog from '@/components/LogoutDialog';
</script>

<template>
  <main>
    <div class="bg-m-grey-500 text-white">
      <div class="px-5 py-5 grid justify-items-center items-center md:grid-cols-5 xl:grid-cols-7">
        <a href=""><img src="@/assets/logo_simple_white.png" class="object-contain col-span-1 w-[10em]"/></a>
        <h1 class="text-5xl sm:text-7xl lg:text-9xl font-title md:col-span-3 xl:col-span-5">FAMILY RECIPES</h1>
      </div>
      <div class="flex justify-end mr-5">
        <a href="">
        <button class="
          text-white 
          font-bold 
          py-2 px-4
          border-r border-b-4 border-m-grey-700 
          hover:border-m-grey-600 hover:bg-m-grey-400 
          rounded-tl-lg">
          user
          </button>
        </a>
        <button class="
          text-white font-bold 
          py-2 px-4 
          border-b-4 border-m-grey-700 
          hover:bg-m-grey-400 hover:border-m-grey-600 
          rounded-tr-lg
          transition
              duration-150
              ease-in-out"
          onclick="openModal('logoutModal')">
          Déconnexion
        </button>
        <a>
        <button class="
          text-white 
          font-bold 
          py-2 px-4
          border-b-4 border-m-grey-700 
          hover:border-m-grey-600 hover:bg-m-grey-400 
          rounded-t-lg">connexion</button>
        </a>
      </div>
    </div>


  </main>
</template>
